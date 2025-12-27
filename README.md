# Poplar Biomass Prediction Model

This repository contains the biostatistical analysis aimed at estimating the biomass (weight) of poplar trees based on non-destructive field measurements (**Diameter** and **Height**).

This project was initially carried out as part of my **Bachelor's degree in Biology (Grenoble Alpes University)** using R, then reproduced in Python to develop my data science skills.

## Project structure

* `data/`: Contains the raw dataset (`.csv`).
* `r_analysis/`: Original analysis script (academic methodology).
* `python_pipeline/`: Counter-expertise and automation performed in Python (Pandas/Statsmodels).

## Statistical Methodology

The study aims to establish an allometric relationship using linear regression.

1.  **Initial Assessment**: The simple linear model ($Weight = a \times ddh + b$) was rejected due to non-normal residuals.
2.  **Transformation**: Application of a **Log-Log transformation** to address non-linearity and heteroscedasticity.
3.  **Validation**: Verification of residual normality ($H_0$: Normality) on the transformed model.

## Main Results

| Metric | Value | Interpretation |
| :--- | :--- | :--- |
| **Adjusted $R^2$** | $0.996$ | **Excellent Fit** (99.6% variance explained) |
| **Shapiro-Wilk** | $0.86$ | **Normality Accepted** ($p > 0.05$) |

**Biological conclusion:**
The Log-Log model is statistically valid and robust. It allows for a reliable estimation of poplar wood yield solely based on diameter and height measurements.

## Tools Used

* **R**: `lm`, `shapiro.test` (Academic standard)
* **Python**: `pandas`, `statsmodels`, `scipy` (Automation & Engineering)

---

*Author: Ismaël PHILIPPE - Biology Student*
