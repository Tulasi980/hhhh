def calculate_parking(hours, vehicle_type, baseline_rate=50, penalty=0):
    # Compute simple duration-based tier
    fee = hours * baseline_rate
    if vehicle_type == "truck":
        fee += 100  # Category extra charge
    if hours > 24:
        fee += penalty  # Multi-day penalty rule
    return {"hours": hours, "total_fee": fee}

print("15:", calculate_parking(5, "truck", 50, 20))
