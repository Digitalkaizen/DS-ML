# Statistical Data Analysis for GoFast Scooter Sharing Service

## Project Overview

GoFast, a scooter-sharing platform project involves statistical analysis of users, trips, and subscription data. The goal is to explore user behavior, test business hypotheses, and provide actionable insights to boost revenue and increase subscriber count.

## Project Objectives

- Load and explore the data
- Preprocess data: fix types, handle missing values and duplicates
- EDA: analyze cities, subscriptions, age, trip distances and durations
- Merge datasets and segment by subscription type
- Calculate revenue per user and per month
- Hypothesis testing:
  - Do subscribed users spend more time riding?
  - Does the average trip exceed 3130 meters?
  - Is monthly revenue from subscribers higher?
  - How to test if support requests decreased after an app update?
- Estimate how many promo codes to send for a marketing campaign
- Model push notification opens using probabilistic distribution

## Dataset Description

**users_go.csv** — user info:
- `user_id` — unique identifier
- `name` — user name
- `age` — age
- `city` — city
- `subscription_type` — subscription plan (`free` / `ultra`)

**rides_go.csv** — trip data:
- `user_id`
- `distance` — distance in meters
- `duration` — duration in minutes
- `date` — trip date

**subscriptions_go.csv** — pricing info:
- `subscription_type`
- `minute_price`
- `start_ride_price`
- `subscription_fee`

## Result

A full analytical overview of user behavior was performed. Key business hypotheses were tested to support strategic decisions in product and marketing. Recommendations were developed to increase revenue and subscriber conversion.
