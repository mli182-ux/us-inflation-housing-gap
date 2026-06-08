# US Inflation and Housing Cost Comparison

## Project Overview

This project compares U.S. overall inflation, housing costs, home values, and household income from 2000 to 2024. The goal is to understand whether housing costs have grown faster than general inflation and income, and what this means for students and young renters.

The project uses public economic data from FRED, Zillow/FRED, and Census/FRED. It includes data downloading, cleaning, visualization, and exploratory regression analysis.

## Research Question

Have U.S. housing costs and home values grown faster than overall inflation and household income since 2000?

## Motivation

Housing affordability is an important economic issue because housing is usually one of the largest expenses for households. For students and young renters, rising housing costs can create additional pressure because they often have lower income, limited savings, and less flexibility in where they live.

This project investigates whether housing costs have grown faster than overall inflation and income, and whether the housing affordability gap has widened over time.

## Data Sources

This project uses publicly available economic time series data:

* FRED CPI All Items
* FRED CPI Shelter
* FRED CPI Rent
* FRED Owners' Equivalent Rent
* Zillow Home Value Index through FRED
* FRED / Census median household income data

## Methods

The project uses Python for data collection, cleaning, visualization, and regression analysis.

Main steps:

1. Download economic time series data from FRED.
2. Convert monthly data into annual averages.
3. Normalize key variables to an index where 2000 = 100.
4. Compare overall inflation, shelter costs, home values, and income growth.
5. Calculate the home value-to-income ratio.
6. Run exploratory OLS regressions.

## Project Structure

```text
us-inflation-housing-gap/
├── data/
│   ├── raw/
│   └── processed/
├── figures/
│   ├── fig1_normalized_trends.png
│   ├── fig2_home_value_to_income.png
│   └── fig3_yoy_growth.png
├── report/
│   ├── one_page_report.md
│   └── regression_summary.txt
├── src/
│   ├── download_data.py
│   ├── clean_data.py
│   ├── make_figures.py
│   └── regression_analysis.py
├── README.md
└── requirements.txt
```

## Key Findings

1. Housing costs and home values grew faster than overall inflation from 2000 to 2024.
2. The home value-to-income ratio increased over time, suggesting that housing became less affordable relative to income.
3. The regression analysis shows a statistically significant positive trend in the home value-to-income gap.
4. The result is especially important for students and young renters because they usually have lower income, less savings, and rely more on rental housing.

## Figure 1: Inflation, Housing Costs, and Income Growth

The first figure compares normalized trends for overall CPI, shelter CPI, rent CPI, Zillow Home Value Index, and median household income. Each series is normalized so that 2000 = 100.

This makes it easier to compare how quickly each variable grew over time.

![Normalized trends](figures/fig1_normalized_trends.png)

The figure shows that home values and shelter-related costs grew faster than overall CPI. This suggests that housing became a larger financial burden relative to general consumer prices.

## Figure 2: Home Value-to-Income Ratio

The second figure shows the ratio between typical home values and median household income.

![Home value to income ratio](figures/fig2_home_value_to_income.png)

This ratio increased over time. For example, the cleaned annual data shows that the ratio was about 3.81 in 2020, increased to about 4.59 in 2022, and remained above 4.3 in 2024. This suggests that the typical home became more expensive relative to the median household's income.

## Figure 3: Year-over-Year Growth

The third figure compares annual growth rates for overall CPI, shelter CPI, home values, and median household income.

![Year-over-year growth](figures/fig3_yoy_growth.png)

The figure shows that home value growth can move differently from general inflation and income growth. Housing growth was especially strong around the post-2020 period.

## Regression Analysis

This project includes two exploratory OLS regression models.

### Model 1: Housing Affordability Gap Over Time

The first regression uses:

```text
log(home value / median household income) ~ year
```

The coefficient on year is positive and statistically significant. This suggests that the home value-to-income gap increased from 2000 to 2024.

### Model 2: Home Value Growth vs. Inflation and Income Growth

The second regression uses:

```text
Zillow Home Value YoY Growth ~ CPI YoY Growth + Income YoY Growth + Post-2020 Indicator
```

This model is weaker statistically, so it should be interpreted carefully. It is useful as a descriptive comparison, but it does not prove that inflation or income growth caused home values to rise.

## Student and Young Renter Impact

Students and young renters are especially affected by rising housing costs because they often have lower income, limited savings, and less stable employment. When rent and housing costs rise faster than income, students may need to live farther from campus, share housing with more roommates, work more hours, or choose schools and internships based partly on housing affordability.

This project does not directly measure individual student rent burdens. Instead, it uses national housing and income trends to show why housing affordability has become a more serious issue for young people and renters.

## Limitations

* The analysis is national-level and does not capture local differences across cities or college towns.
* Zillow home values measure home prices, not monthly mortgage payments.
* Shelter CPI and Zillow home values measure different aspects of housing costs.
* Student impact is discussed as an implication, not directly measured with student-level data.
* The regression analysis is descriptive and does not prove causality.

## How to Run This Project

Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Download data:

```bash
python3 src/download_data.py
```

Clean and merge data:

```bash
python3 src/clean_data.py
```

Create figures:

```bash
python3 src/make_figures.py
```

Run regression analysis:

```bash
python3 src/regression_analysis.py
```

## Conclusion

From 2000 to 2024, U.S. housing costs and home values grew faster than general inflation and household income. The home value-to-income ratio increased over time, suggesting that housing affordability worsened. This trend is especially important for students and young renters because they depend heavily on rental markets and often have limited income flexibility.

Overall, the project shows that housing affordability is not only a general inflation issue. Housing has grown faster than many other prices and has become a major source of economic pressure for younger households.
