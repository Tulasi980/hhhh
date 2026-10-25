def optimize_basket(basket, budget):
    # Process items sequentially and reduce quantities if above total budget ceiling
    for item in basket:
        while item["qty"] > 0:
            total = 0
            for i in basket:
                total += i["qty"] * i["price"]
            if total <= budget:
                break
            item["qty"] -= 1
    return basket

print("19:", optimize_basket([{"name": "Shoes", "price": 2000, "qty": 2}, {"name": "Shirt", "price": 1000, "qty": 2}], 4500))
