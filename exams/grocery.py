def shop_from_grocery_list(my_budget, *args):
    budget = float(my_budget)
    list_of_products = args[0]
    purchased = set()

    for product, price in args[1:]:
        if product in list_of_products and product not in purchased:
            if price <= budget:
                budget -= price
                purchased.add(product)
            else:
                break
    if len(purchased) == len(list_of_products):
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        missing_products = [el for el in list_of_products if el not in purchased]
        return f"You did not buy all the products. Missing products: {', '.join(missing_products)}."


print(shop_from_grocery_list(100, ["tomato", "cola"], ("cola", 5.8), ("tomato", 10.0), ("tomato", 20.45)))
