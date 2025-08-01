# Исследование объявлений о продаже квартир

## Описание проекта

Проект: Исследовательский анализ данных.  
Цель: определить параметры, влияющие на рыночную стоимость объектов недвижимости.  
Данные: архив объявлений о продаже квартир в Санкт-Петербурге и соседних населённых пунктах, предоставленный Яндекс Недвижимость.

## Задачи

- Изучить структуру и особенности данных.
- Выполнить предобработку: заполнение пропусков, удаление дубликатов, приведение типов.
- Добавить новые признаки: цена за квадратный метр, день/месяц/год публикации, категория этажа и др.
- Исследовать влияние параметров (общая/жилая/кухонная площадь, этаж, дата размещения, количество комнат) на цену.
- Оценить зависимость цены от расстояния до центра города.
- Построить таблицы и графики для анализа:
    - средней цены за м² по населенным пунктам;
    - средней цены в зависимости от расстояния до центра;
    - времени экспозиции объявлений;
    - факторов, влияющих на цену.

## Результат

Построена система EDA-анализа, выявлены параметры, влияющие на цену недвижимости, сформированы графики зависимости цены от ключевых факторов. Подготовлены данные для модели ценообразования и выявления аномалий.

## Описание данных

- `total_area` — общая площадь
- `last_price` — цена
- `rooms` — количество комнат
- `ceiling_height` — высота потолков
- `floors_total`, `floor` — этажность
- `cityCenters_nearest` — расстояние до центра
- `first_day_exposition` — дата публикации
- `days_exposition` — срок размещения
- `locality_name` — населённый пункт
- `kitchen_area`, `living_area` — площадь кухни и жилая
- `parks_nearest`, `ponds_nearest` — расстояния до объектов
