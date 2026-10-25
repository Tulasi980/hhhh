def simulate_atm(balance, tx_list, daily_limit=50000):
    total_withdrawn = 0
    summary = []
    for tx_type, amt in tx_list:
        if amt <= 0:
            status = "Rejected"
        elif tx_type == "deposit":
            balance += amt
            status = "Success"
        elif tx_type == "withdraw":
            if amt > balance or total_withdrawn + amt > daily_limit:
                status = "Rejected"
            else:
                balance -= amt
                total_withdrawn += amt
                status = "Success"
        summary.append(tx_type + ": " + status)
    return {"balance": balance, "history": summary}

print("13:", simulate_atm(10000, [("withdraw", 4000), ("deposit", 2000)]))
