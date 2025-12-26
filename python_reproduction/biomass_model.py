import pandas as pd
import numpy as np
import statsmodels.api as sm
from scipy import stats
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, '..', 'data', 'poplar_raw_data.csv')

df_raw = pd.read_csv(file_path)

print("--- DATA PREVIEW (RAW) ---")
print(df_raw.head())
print("-" * 30)

df = df_raw[(df_raw['Age'] == 3) & (df_raw['Year'] == 1) & (df_raw['Treatment'] == 1)].copy()

# Simulating the correction of the data. Optionnal
df.loc[df['TreeID'] == 15, 'Diameter'] = 2.9

df['ddh'] = (df['Diameter'] ** 2) * df['Height']

df['log_weight'] = np.log(df['Weight'])
df['log_ddh'] = np.log(df['ddh'])

print("\n--- OLS REGRESSION RESULTS (LOG-LOG MODEL) ---")
X = df['log_ddh']
X = sm.add_constant(X)
y = df['log_weight']

model = sm.OLS(y, X).fit()
print(model.summary())

print("\n--- RESIDUALS NORMALITY TEST (SHAPIRO-WILK) ---")
residuals = model.resid
shapiro_stat, shapiro_p = stats.shapiro(residuals)

print(f"Statistic: {shapiro_stat:.5f}")
print(f"P-value:   {shapiro_p:.5f}")

if shapiro_p > 0.05:
    print("Result: Residuals follow a normal distribution. Model is valid.")
else:
    print("Result: Residuals do not follow a normal distribution.")
