import matplotlib.pyplot as plt

# Sample vehicle count data
vehicle_counts = [5, 12, 18, 25, 30, 22, 15, 8]

# Frame/time labels
time_intervals = [1, 2, 3, 4, 5, 6, 7, 8]

# Create graph
plt.plot(time_intervals, vehicle_counts, marker='o')

# Labels
plt.title("Traffic Density Analysis")
plt.xlabel("Time Interval")
plt.ylabel("Vehicle Count")

# Show grid
plt.grid(True)

# Display graph
plt.show()