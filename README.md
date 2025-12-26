# Poplar Biomass Prediction Model

This repository contains a biostatistical analysis aimed at estimating the biomass (weight) of poplar trees based on non-destructive field measurements (diameter and height).

The project demonstrates the application of linear regression models, data transformation techniques (Log-Log), and model validation. It was originally conducted in R during a Licence 3 Biology course (Universite Grenoble Alpes) and reproduced in Python to showcase Data Science capabilities.

## Project Structure

* data/: Contains the raw dataset.
* r_analysis/: Original R script following the academic methodology.
* python_reproduction/: Python implementation using statsmodels and pandas for data processing and modeling.

## Methodology

### 1. Biological Question
Is it possible to reliably estimate the weight of a tree (and thus its wood yield) solely from its height and diameter?

### 2. Statistical Approach
The initial simple linear regression model ($Weight = a \times ddh + b$) was rejected due to non-normal residuals. A logarithmic transformation was applied to correct non-linearity and heteroscedasticity.

* **Target Variable:** log(Weight)
* **Predictor Variable:** log(Diameter² * Height)
* **Validation:** Shapiro-Wilk test on residuals and analysis of R-squared.

## Key Results

The Log-Log model proved to be highly effective compared to the raw linear model:

* **Adjusted R-squared:** 0.996 (The model explains 99.6% of the variance).
* **Significance:** The predictor variable is statistically significant (p < 0.001).
* **Model Validity:** The residuals of the transformed model follow a normal distribution (Shapiro-Wilk p-value = 0.86), validating the statistical inference.

## Tech Stack

* **R:** lm (Linear Models), shapiro.test
* **Python:**
    * **Pandas:** Data filtering and feature engineering.
    * **NumPy:** Logarithmic transformations.
    * **Statsmodels:** OLS regression and statistical summaries.
    * **SciPy:** Normality testing.

---
Author: Ismael PHILIPPE
