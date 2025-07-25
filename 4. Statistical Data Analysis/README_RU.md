# Статистический анализ данных для сервиса аренды самокатов GoFast

## Описание проекта

В рамках проекта сервиса аренды самокатов GoFast проводится статистический анализ данных пользователей, поездок и условий подписки. Цель — понять поведение клиентов, проверить гипотезы и предложить рекомендации для увеличения выручки и доли подписчиков.

## Задачи проекта

- Загрузка и первичный анализ данных
- Предобработка: типы данных, пропуски, дубликаты
- EDA: анализ городов, подписок, возраста, расстояний и продолжительности поездок
- Объединение таблиц и сегментация по подписке
- Подсчёт выручки по пользователям и по месяцам
- Проверка гипотез:
  - Тратят ли пользователи с подпиской больше времени?
  - Превышает ли среднее расстояние поездки 3130 м?
  - Выручка от подписчиков выше, чем от остальных?
  - Как проверить снижение обращений в поддержку после обновлений?
- Расчёт необходимого числа промокодов для достижения цели маркетинга
- Аппроксимация распределения открытий push-уведомлений

## Описание данных

**users_go.csv** — информация о пользователях:
- `user_id` — уникальный идентификатор
- `name` — имя
- `age` — возраст
- `city` — город
- `subscription_type` — тип подписки (`free` / `ultra`)

**rides_go.csv** — данные о поездках:
- `user_id`
- `distance` — расстояние (м)
- `duration` — длительность (мин)
- `date` — дата поездки

**subscriptions_go.csv** — информация о тарифах:
- `subscription_type`
- `minute_price` — цена за минуту
- `start_ride_price` — цена старта
- `subscription_fee` — ежемесячная плата

## Результат

Получен полный аналитический обзор клиентов и их поведения. Проверены ключевые гипотезы для поддержки принятия решений бизнесом и маркетингом. Сформулированы рекомендации по увеличению выручки и числа пользователей с подпиской.
