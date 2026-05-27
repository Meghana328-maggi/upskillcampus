def analyze_traffic(vehicle_count):

    if vehicle_count < 10:
        density = "Low"
        signal_time = 20

    elif vehicle_count < 25:
        density = "Medium"
        signal_time = 40

    else:
        density = "High"
        signal_time = 60

    return density, signal_time


# Example Testing
vehicle_count = 32

density, signal = analyze_traffic(vehicle_count)

print("Vehicle Count:", vehicle_count)
print("Traffic Density:", density)
print("Recommended Signal Time:", signal, "seconds")