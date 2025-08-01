# Проект: Прогнозирование заказов такси

## Описание проекта

Компания собрала исторические данные о заказах такси в аэропортах. Чтобы привлекать больше водителей в период пиковой нагрузки, необходимо спрогнозировать количество заказов такси на следующий час. Цель проекта — построить модель машинного обучения для такого предсказания.

**Целевое условие:** значение метрики RMSE на тестовой выборке должно быть **не больше 48**.

---

## Этапы проекта

1. Загрузка и предобработка данных:
   - Ресемплирование данных по одному часу;
   - Анализ временного ряда.

2. Обучение моделей:
   - Построение нескольких моделей с разными гиперпараметрами;
   - Разделение выборки: 10% — тестовая.

3. Оценка качества:
   - Проверка качества модели на тестовой выборке;
   - Выводы и интерпретация результатов.

---

## Описание данных

Датасет расположен в файле: `/datasets/taxi.csv`.

- **num_orders** — количество заказов (целевой признак);
- Временная метка (datetime index) используется в качестве индекса.

---

## Используемые технологии

- Pandas
- Scikit-learn
- Matplotlib / Seaborn
- Временные ряды
- Модели машинного обучения: Linear Regression, Random Forest, Gradient Boosting и др.