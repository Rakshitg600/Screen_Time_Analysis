import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
file_path = 'screen_time_data.csv'  # Update path if needed
data = pd.read_csv(file_path)

# Group by hour and calculate total usage for distracting apps
distracting_data = data[data['Distracting'] == True]
hourly_usage = distracting_data.groupby('Start Hour')['Usage Time (minutes)'].sum()

# Normalize data to find relative usage per hour
hourly_usage_normalized = hourly_usage / hourly_usage.sum()

# Use NumPy for additional statistical calculations
total_usage_mean = np.mean(hourly_usage)
total_usage_std = np.std(hourly_usage)
print(f"Mean usage (minutes): {total_usage_mean:.2f}")
print(f"Standard deviation of usage (minutes): {total_usage_std:.2f}")

# Plot
plt.figure(figsize=(12, 6))
sns.barplot(x=hourly_usage_normalized.index, y=hourly_usage_normalized.values, palette="viridis")
plt.title('Normalized Screen Time of Distracting Apps by Hour', fontsize=16)
plt.xlabel('Hour of the Day', fontsize=14)
plt.ylabel('Relative Usage (%)', fontsize=14)
plt.xticks(range(0, 24))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Show the plot
plt.show()

# Highlight most and least predictive hours
most_predictive_hour = hourly_usage.idxmax()
least_predictive_hour = hourly_usage.idxmin()

print(f"Most predictive hour (highest distracting usage): {most_predictive_hour}:00")
print(f"Least predictive hour (lowest distracting usage): {least_predictive_hour}:00")
