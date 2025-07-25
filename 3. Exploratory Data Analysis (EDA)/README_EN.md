# Real Estate Listings Analysis

## Project Overview

Project type: Exploratory Data Analysis (EDA).  
Goal: Identify key factors that influence the market value of real estate properties.  
Dataset: Archive of apartment sale listings from Yandex Real Estate for Saint Petersburg and nearby localities.

## Objectives

- Explore the dataset structure and distributions.
- Perform data preprocessing: handle missing values, remove duplicates, convert data types.
- Engineer new features: price per square meter, publication weekday/month/year, floor category, etc.
- Investigate how parameters (total/living/kitchen area, floor, listing date, number of rooms) affect the price.
- Assess how price depends on the distance from the city center.
- Build summary tables and plots:
    - average price per m² by locality;
    - average price vs. distance to center;
    - listing exposition duration;
    - key price impact factors.

## Result

Developed a robust EDA pipeline, identified significant features affecting property prices, visualized pricing trends, and prepared data for pricing models and anomaly detection.

## Data Description

- `total_area` — total area
- `last_price` — listing price
- `rooms` — number of rooms
- `ceiling_height` — ceiling height
- `floors_total`, `floor` — number of floors, floor level
- `cityCenters_nearest` — distance to city center
- `first_day_exposition` — listing date
- `days_exposition` — time on market
- `locality_name` — locality name
- `kitchen_area`, `living_area` — kitchen and living area
- `parks_nearest`, `ponds_nearest` — distance to parks and ponds
