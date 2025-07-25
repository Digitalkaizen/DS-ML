# Проект: Выбор региона для разработки новой нефтяной скважины

## Описание проекта

В добывающей компании нужно решить, где бурить новую скважину. Цель проекта — построить модель для определения региона, где добыча принесёт наибольшую прибыль. На основании исторических данных по трём регионам будет проведён анализ, обучение модели и оценка прибыли и рисков с помощью техники bootstrap.

## Этапы проекта

### 1. Загрузка и подготовка данных
- Импорт данных из трёх регионов.
- Проверка данных на пропуски и дубликаты.
- Разделение данных на признаки и целевой признак.

### 2. Обучение моделей
- Разделение на обучающую и валидационную выборки (75:25).
- Обучение модели линейной регрессии.
- Предсказания и расчет метрик (RMSE, средний запас).

### 3. Подготовка к расчёту прибыли
- Расчет достаточного объёма сырья для безубыточности.
- Сравнение с реальными средними запасами в регионах.

### 4. Расчет прибыли
- Выбор 200 лучших точек по предсказаниям.
- Расчёт прибыли от выбранных скважин.

### 5. Bootstrap-анализ
- 1000 итераций выбора случайных скважин.
- Расчет доверительного интервала и среднего значения прибыли.
- Оценка риска убытков.

## Условия задачи

- Используется только линейная регрессия.
- Разработка 200 скважин из 500 выбранных.
- Бюджет: 10 млрд рублей.
- Доход с 1 тыс. баррелей: 450 тыс. рублей.
- Риски: допускается не более 2.5% вероятности убытков.

## Выводы

Результаты bootstrap-анализа позволяют выбрать регион с наибольшей ожидаемой прибылью при допустимом уровне риска. Этот регион рекомендуется для разработки.