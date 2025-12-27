# Biomass Prediction Model
# Context: Bio-statistics L3
# Objective: Estimate poplar weight based on dendrometric measurements using Log-Log regression.

# 1. Data Loading
raw_data <- read.csv("../data/poplar_raw_data.csv")

# 2. Subsetting
poplar_data <- subset(raw_data, Age == 3 & Year == 1 & Treatment == 1)

# 3. Feature Engineering
poplar_data$ddh <- (poplar_data$Diameter^2) * poplar_data$Height

# Log-Log transformation 
poplar_data$log_weight <- log(poplar_data$Weight)
poplar_data$log_ddh <- log(poplar_data$ddh)

# 4. Model Fitting
# Linear Model: log(Weight) = a * log(ddh) + b 
model_log <- lm(log_weight ~ log_ddh, data = poplar_data)

print(summary(model_log))

# 5. Model Validation (Residuals)
# H0: Residuals follow a normal distribution.
shapiro_res <- shapiro.test(residuals(model_log))

print(shapiro_res)

# Interpretation:
# p-value (0.8606) > 0.05 -> H0 Accepted. The residuals are normal.
