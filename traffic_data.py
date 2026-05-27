import pandas as pd

# Sample traffic data
data = {
    "Time Interval": [1, 2, 3, 4, 5],
    "Vehicle Count": [8, 15, 28, 35, 12],
    "Traffic Density": ["Low", "Medium", "High", "High", "Medium"],
    "Signal Time": [20, 40, 60, 60, 40]
}

# Create dataframe
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("traffic_data.csv", index=False)

print("Traffic data saved successfully!")