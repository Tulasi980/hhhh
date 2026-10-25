def analyze_performance(students):
    report = {}
    for name in students:
        scores = students[name]
        is_improving = True
        # Check if every exam score is equal to or better than the last
        for i in range(1, len(scores)):
            if scores[i] < scores[i-1]:
                is_improving = False
        report[name] = "Improving" if is_improving else "Inconsistent"
    return report

print("17:", analyze_performance({"Alice":, "Bob": [80, 78, 82]}))
