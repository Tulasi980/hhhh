def find_best_route(distance, fuel_price, vehicles):
    best_car = ""
    lowest_cost = 99999999
    for name in vehicles:
        v = vehicles[name]
        fuel_needed = (distance / v["mileage"]) + v["reserve"]
        cost = fuel_needed * fuel_price
        if cost < lowest_cost:
            lowest_cost = cost
            best_car = name
    return {"car": best_car, "cost": lowest_cost}

print("18:", find_best_route(300, 100, {"SUV": {"mileage": 10, "reserve": 5}, "Sedan": {"mileage": 15, "reserve": 3}}))
