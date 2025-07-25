# Обучение с учителем: модель для предсказания снижения покупательской активности

## Описание проекта

Интернет-магазин «В один клик» фиксирует снижение активности постоянных клиентов.  
Цель проекта — построить модель, которая предсказывает вероятность снижения покупательской активности в течение следующих 3 месяцев.  
На основе модели нужно выделить сегменты покупателей и разработать персонализированные предложения.

## Используемые данные

- `market_file.csv` — признаки взаимодействия с клиентом, поведения на сайте и продуктового поведения.
- `market_money.csv` — выручка клиента за периоды.
- `market_time.csv` — время, проведённое на сайте.
- `money.csv` — прибыль от клиента за последние 3 месяца.

## Этапы проекта

1. **Загрузка и проверка данных** — анализ структуры и соответствия описанию.
2. **Предобработка** — обработка пропусков, типов, фильтрация клиентов с недостаточной активностью.
3. **EDA** — исследовательский анализ каждого источника данных.
4. **Объединение таблиц** — сведение данных в единую таблицу с разными периодами.
5. **Корреляционный анализ** — проверка мультиколлинеарности и удаление избыточных признаков.
6. **Обучение моделей**:
   - Модели: KNN, DecisionTree, LogisticRegression, SVC
   - Использование пайплайнов с разными трансформерами и скейлерами
   - Подбор гиперпараметров и выбор лучшей модели по ROC-AUC
7. **Анализ важности признаков**:
   - Интерпретация с помощью SHAP
   - Выделение ключевых и второстепенных факторов
8. **Сегментация клиентов**:
   - Сегмент с высокой вероятностью снижения активности и высокой прибылью
   - Графический и аналитический разбор
   - Предложения по удержанию

## Результат

- Построена модель с высокой точностью предсказания (метрика ROC-AUC).
- Выделены ключевые признаки, влияющие на снижение активности.
- Разработаны рекомендации для персонализированных действий по удержанию клиентов.
