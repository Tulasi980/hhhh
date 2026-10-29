
def calculate_parking(hours, vehicle_type, baseline_rate=50, penalty=0):
    fee = hours * baseline_rate
    if vehicle_type == "truck":
        fee += 100  
    if hours > 24:
        fee += penalty  
    return {"hours": hours, "total_fee": fee}

print("15:", calculate_parking(5, "truck", 50, 20))


