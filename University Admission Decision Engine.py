def university_admission(candidates, min_agg, math_cut):
    eligible = []
    for c in candidates:
        if c["agg"] >= min_agg and c["math"] >= math_cut:
            eligible.append(c)
    # Manual sort: Tier 1 Math Score, Tier 2 Aggregate
    for i in range(len(eligible)):
        for j in range(i + 1, len(eligible)):
            if (eligible[j]["math"] > eligible[i]["math"]) or (eligible[j]["math"] == eligible[i]["math"] and eligible[j]["agg"] > eligible[i]["agg"]):
                eligible[i], eligible[j] = eligible[j], eligible[i]
    return eligible

candidates = [{"id": 1, "agg": 85, "math": 90}, {"id": 2, "agg": 88, "math": 85}]
print("20:", university_admission(candidates, 80, 80))
