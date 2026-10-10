import numpy as np

# ==========================================
# TEXTILE MILL SENSOR DATA ANALYZER
# ==========================================

# 1. Sensor Data
temperature = np.array([30, 32, 31, 35, 33])
humidity = np.array([60, 65, 70, 75, 68])
machine_speed = np.array([1200, 1250, 1180, 1300, 1270])


# 2. Temperature Analysis
average_temperature = np.mean(temperature)
maximum_temperature = np.max(temperature)
minimum_temperature = np.min(temperature)
temperature_range = maximum_temperature - minimum_temperature
temperature_std = np.std(temperature)
median_temperature = np.median(temperature)


# 3. Humidity Analysis
average_humidity = np.mean(humidity)


# 4. Machine Speed Analysis
average_speed = np.mean(machine_speed)
maximum_speed = np.max(machine_speed)
minimum_speed = np.min(machine_speed)


# 5. Boolean Masking
high_temperature = temperature > 33
high_humidity = humidity >= 70
high_speed = machine_speed > 1250

high_temperature_values = temperature[high_temperature]
high_humidity_values = humidity[high_humidity]
high_speed_values = machine_speed[high_speed]


# 6. Count Warning Conditions
dangerous_temperature = temperature >= 35
dangerous_temperature_count = np.sum(dangerous_temperature)

high_humidity_count = np.sum(high_humidity)


# 7. Reshaping
temperature_2d = temperature.reshape(1, 5)
temperature_column = temperature.reshape(5, 1)


# 8. Missing Data / NaN Handling
temperature_with_nan = np.array([30, 32, np.nan, 35, 33])

average_with_nan = np.mean(temperature_with_nan)
average_without_nan = np.nanmean(temperature_with_nan)

missing_values = np.isnan(temperature_with_nan)
missing_value_count = np.sum(missing_values)


# 9. Broadcasting
adjusted_temperature = temperature + 2


# 10. Combined Sensor Data
sensor_data = np.array([temperature, humidity, machine_speed])
sensor_shape = sensor_data.shape
sensor_averages = np.mean(sensor_data, axis=1)


# 11. Final Results
print("===== TEXTILE MILL SENSOR DATA ANALYZER =====")

print("\n--- Temperature ---")
print("Average:", average_temperature)
print("Maximum:", maximum_temperature)
print("Minimum:", minimum_temperature)
print("Range:", temperature_range)
print("Standard Deviation:", temperature_std)
print("Median:", median_temperature)

print("\n--- Humidity ---")
print("Average:", average_humidity)

print("\n--- Machine Speed ---")
print("Average:", average_speed)
print("Maximum:", maximum_speed)
print("Minimum:", minimum_speed)

print("\n--- Warning Conditions ---")
print("High Temperatures:", high_temperature_values)
print("High Humidity:", high_humidity_values)
print("High Machine Speeds:", high_speed_values)
print("Dangerous Temperature Count:", dangerous_temperature_count)
print("High Humidity Count:", high_humidity_count)

print("\n--- Missing Data ---")
print("Average with NaN:", average_with_nan)
print("Average ignoring NaN:", average_without_nan)
print("Missing Values:", missing_value_count)

print("\n--- Combined Sensor Data ---")
print("Sensor Data Shape:", sensor_shape)
print("Sensor Averages:", sensor_averages)

print("\n--- Broadcasting ---")
print("Adjusted Temperature:", adjusted_temperature)