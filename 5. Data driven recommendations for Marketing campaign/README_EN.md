# Identifying Factors That Determine Game Success

## Project Overview

International game store "Stream".  
Provided with historical data on game sales, user and critic scores, platforms, and genres.  
The goal is to identify patterns that determine game success and provide data-driven recommendations for the 2017 advertising campaign.

## Project Stages

1. Load and explore the dataset (`games.csv`)
2. Data preprocessing:
   - Standardize column names (lowercase)
   - Handle missing values and anomalies (e.g., 'tbd' in `user_score`)
   - Create a `total_sales` column (sum of all regional sales)
3. Exploratory analysis:
   - Number of games released per year
   - Sales dynamics by platform and platform lifecycle
   - Influence of critic and user reviews on sales
   - Genre profitability
4. User profiles by region (NA, EU, JP):
   - Top platforms and genres
   - Impact of ESRB rating on regional sales
5. Hypothesis testing:
   - Equality of average user scores for Xbox One and PC
   - Difference in average scores for Action and Sports genres
6. Final conclusions and recommendations

## Dataset Description

- `name` — game title
- `platform` — platform (e.g., PS4, Xbox)
- `year_of_release` — year of release
- `genre` — game genre
- `na_sales`, `eu_sales`, `jp_sales`, `other_sales` — regional sales (in millions)
- `critic_score` — critic score (0–100)
- `user_score` — user score (0–10)
- `rating` — ESRB rating (age restriction category)

## Result

Key factors influencing game popularity by platform, genre, and region were identified.  
Statistical hypotheses were tested.  
Recommendations were generated to support marketing strategy.
