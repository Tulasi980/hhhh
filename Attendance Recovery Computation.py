def recovery_steps(attended, total, threshold=0.75):
    current = attended / total
    needed = 0
    
    while (attended + needed) / (total + needed) < threshold:
        needed += 1
    return {"current": current, "consecutive_needed": needed}

print("12:", recovery_steps(12, 20, 0.75))
