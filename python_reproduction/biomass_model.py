"""
Poplar Biomass Prediction Pipeline
Automates the training and validation of an allometric log-log regression model.
"""

from pathlib import Path
from typing import Dict
import pandas as pd
import numpy as np
import statsmodels.api as sm
from scipy import stats

# --- Configuration ---
ALPHA = 0.05
TARGET_COHORT = {'Age': 3, 'Year': 1, 'Treatment': 1}

def load_data(relative_path: str) -> pd.DataFrame:
    """Loads CSV data relative to the script location."""
    base_path = Path(__file__).resolve().parent
    data_path = base_path / relative_path
    
    if not data_path.exists():
        raise FileNotFoundError(f"Dataset not found at: {data_path}")
    
    return pd.read_csv(data_path)

def preprocess_cohort(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filters the specific cohort and applies known data corrections.
    """
    # 1. Filter Cohort
    mask = (
        (df['Age'] == TARGET_COHORT['Age']) & 
        (df['Year'] == TARGET_COHORT['Year']) & 
        (df['Treatment'] == TARGET_COHORT['Treatment'])
    )
    df_clean = df[mask].copy()
    
    # 2. Feature Engineering
    # Variable 'ddh' = Diameter^2 * Height
    df_clean['ddh'] = (df_clean['Diameter'] ** 2) * df_clean['Height']
    
    # 3. Log Transformation
    df_clean['log_weight'] = np.log(df_clean['Weight'])
    df_clean['log_ddh'] = np.log(df_clean['ddh'])
    
    return df_clean

def run_regression_analysis(df: pd.DataFrame) -> Dict:
    """
    Fits OLS model and performs Shapiro-Wilk test on residuals.
    """
    X = df['log_ddh']
    X = sm.add_constant(X)
    y = df['log_weight']
    
    # Fit Model
    model = sm.OLS(y, X).fit()
    
    # Normality Test
    residuals = model.resid
    shapiro_stat, shapiro_p = stats.shapiro(residuals)
    
    return {
        "params": model.params,
        "r_squared": model.rsquared,
        "f_pvalue": model.f_pvalue,
        "shapiro_stat": shapiro_stat,
        "shapiro_p": shapiro_p,
        "n_obs": int(model.nobs)
    }

def print_portfolio_report(results: Dict):
    """Prints a formatted report matching the PDF conclusions."""
    print("-" * 50)
    print("POPLAR BIOMASS MODEL REPORT (Log-Log)")
    print("-" * 50)
    
    print(f"Data Points:      {results['n_obs']}")
    print(f"R-Squared:        {results['r_squared']:.4f}")
    print(f"Intercept:        {results['params']['const']:.4f}")
    print(f"Slope (log_ddh):  {results['params']['log_ddh']:.4f}")
    
    print("-" * 50)
    print("VALIDATION DIAGNOSTICS")
    print(f"Shapiro-Wilk P:   {results['shapiro_p']:.4f} (Target: 0.8606)")
    
    if results['shapiro_p'] > ALPHA:
        print(">> CONCLUSION: Residuals are NORMAL. Model is VALID.")
    else:
        print(">> CONCLUSION: Residuals are NOT normal. Model INVALID.")
    print("-" * 50)

# --- Main Execution Entry Point ---
if __name__ == "__main__":
    try:
        # 1. Load
        raw_df = load_data('../data/poplar_raw_data.csv')
        
        # 2. Process
        clean_df = preprocess_cohort(raw_df)
        
        # 3. Analyze
        results = run_regression_analysis(clean_df)
        
        # 4. Report
        print_portfolio_report(results)
        
    except Exception as e:
        print(f"Pipeline Error: {e}")
