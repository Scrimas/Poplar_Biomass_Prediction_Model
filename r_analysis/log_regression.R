raw_data <- read.csv("../data/poplar_raw_data.csv")

poplar_data <- subset(raw_data, Age == 3 & Year == 1 & Treatment == 1)

poplar_data[poplar_data$TreeID == 15, "Diameter"] <- 2.9

poplar_data$ddh <- (poplar_data$Diameter^2) * poplar_data$Height

poplar_data$log_weight <- log(poplar_data$Weight)
poplar_data$log_ddh <- log(poplar_data$ddh)

model_log <- lm(log_weight ~ log_ddh, data = poplar_data)

print(summary(model_log))

shapiro_res <- shapiro.test(residuals(model_log))
print(shapiro_res)
