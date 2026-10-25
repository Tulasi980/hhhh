def simulate_tank(capacity, initial, schedule, threshold):
    level = initial
    step_reached = -1
    index = 1
    for inflow, outflow in schedule:
        level = level + inflow - outflow
        if level > capacity:
            level = capacity
        if level < 0:
            level = 0
        if level >= threshold and step_reached == -1:
            step_reached = index
        index += 1
    return {"final_level": level, "step": step_reached}

print("16:", simulate_tank(1000, 200, [(300, 100), (500, 50)], 700))
