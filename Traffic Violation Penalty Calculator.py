def calculate_fines(violations, base_rules):
    total = 0
    disqualified = False
    for v_type, is_repeat in violations:
        fine = base_rules[v_type]
        if is_repeat:
            fine = fine * 2  
        total += fine
        if v_type == "DUI":
            disqualified = True
    return {"total": total, "banned": disqualified}

rules = {"Speeding": 2000, "DUI": 10000}
print("21:", calculate_fines([("Speeding", True), ("DUI", False)], rules))
