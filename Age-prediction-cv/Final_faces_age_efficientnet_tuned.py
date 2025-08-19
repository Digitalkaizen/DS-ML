import os
import pandas as pd
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, BatchNormalization, Dropout
from tensorflow.keras.optimizers import Adam, SGD
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
from tensorflow.keras.losses import Huber

# 1) ЗАГРУЗКА ДАННЫХ

def _make_datagen(is_train=True, val_split=0.2):
    if is_train:
        # лёгкая аугментация + нормализация
        return ImageDataGenerator(
            rescale=1./255.,
            validation_split=val_split,
            horizontal_flip=True,
            zoom_range=0.1,
            width_shift_range=0.1,
            height_shift_range=0.1,
            brightness_range=(0.8, 1.2)
        )
    else:
        return ImageDataGenerator(rescale=1./255.)

def load_train(path, image_size=(224, 224), batch_size=32, val_split=0.2, seed=42):
    """
    Читает labels.csv и строит генератор ТРЕНИРОВОЧНОЙ части через flow_from_dataframe().
    Возвращает DataFrameIterator.
    """
    df = pd.read_csv(os.path.join(path, 'labels.csv'))
    datagen = _make_datagen(is_train=True, val_split=val_split)

    train_flow = datagen.flow_from_dataframe(
        dataframe=df,
        directory=os.path.join(path, 'final_files'),
        x_col='file_name',
        y_col='real_age',
        target_size=image_size,
        color_mode='rgb',
        class_mode='raw',          # регрессия!
        batch_size=batch_size,
        subset='training',
        shuffle=True,
        seed=seed
    )
    return train_flow

def load_test(path, image_size=(224, 224), batch_size=32, val_split=0.2, seed=42):
    """
    Читает labels.csv и строит генератор ВАЛИДАЦИОННОЙ/ТЕСТОВОЙ части через flow_from_dataframe().
    Возвращает DataFrameIterator.
    """
    df = pd.read_csv(os.path.join(path, 'labels.csv'))
    datagen = _make_datagen(is_train=True, val_split=val_split)

    val_flow = datagen.flow_from_dataframe(
        dataframe=df,
        directory=os.path.join(path, 'final_files'),
        x_col='file_name',
        y_col='real_age',
        target_size=image_size,
        color_mode='rgb',
        class_mode='raw',
        batch_size=batch_size,
        subset='validation',
        shuffle=False,
        seed=seed
    )
    return val_flow

# 2) МОДЕЛЬ

def create_model(input_shape=(224, 224, 3), n_hidden=128, dropout_top=0.3):
    """
    ResNet50 (замороженный) + лёгкая «голова».
    Сразу подгружаем веса с сервера, чтобы не тянуть из интернета.
    """
    weights_path = '/datasets/keras_models/resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5'
    backbone = ResNet50(
        include_top=False,
        weights=weights_path if os.path.exists(weights_path) else 'imagenet',
        input_shape=input_shape
    )
    backbone.trainable = False  # первый этап — на «заморозке»

    model = Sequential([
        backbone,
        GlobalAveragePooling2D(),
        BatchNormalization(),
        Dropout(dropout_top),
        Dense(n_hidden, activation='relu'),
        BatchNormalization(),
        Dropout(dropout_top),
        Dense(1, activation='relu')  # возраст >= 0
    ])

    # быстрый старт: MSE быстрее оптимизируется
    model.compile(optimizer=Adam(learning_rate=1e-3), loss='mse', metrics=['mae'])
    return model

# 3) ОБУЧЕНИЕ (двухфазное с fine-tuning)

def train_model(model, train_data, test_data,
                batch_size=None, epochs=12,
                steps_per_epoch=None, validation_steps=None):
    """
    1) Прогрев (замороженный бэкбон): ~40% эпох.
    2) Разморозка хвоста ResNet50 и дообучение с маленьким lr и Huber loss.
    ВНИМАНИЕ: для генераторов batch_size в model.fit НЕ передаём.
    """
    # коллбеки (одни и те же на обе фазы) ---
    es = EarlyStopping(monitor='val_mae', mode='min', patience=3, restore_best_weights=True, verbose=1)
    rlrop = ReduceLROnPlateau(monitor='val_mae', mode='min', factor=0.5, patience=2, verbose=1, min_lr=1e-6)

    warmup_epochs = max(2, int(0.4 * epochs))
    finetune_epochs = max(epochs - warmup_epochs, 1)

    # Фаза 1: замороженный бэкбон
    model.fit(
        train_data,
        validation_data=test_data,
        epochs=warmup_epochs,
        steps_per_epoch=steps_per_epoch,
        validation_steps=validation_steps,
        verbose=2,
        callbacks=[es, rlrop]
    )

    # Фаза 2: fine-tuning хвоста
    # найти бэкбон (первый слой Sequential)
    backbone = model.layers[0]
    # размораживаем последние 50 слоёв
    n_unfreeze = 50
    for layer in backbone.layers[-n_unfreeze:]:
        layer.trainable = True
    backbone.trainable = True

    # пере-компиляция: маленький шаг, SGD+momentum, Huber устойчив к шуму
    model.compile(
        optimizer=SGD(learning_rate=1e-5, momentum=0.9, nesterov=True),
        loss=Huber(delta=5.0),
        metrics=['mae']
    )

    model.fit(
        train_data,
        validation_data=test_data,
        epochs=finetune_epochs,
        steps_per_epoch=steps_per_epoch,
        validation_steps=validation_steps,
        verbose=2,
        callbacks=[es, rlrop]
    )

    return model
