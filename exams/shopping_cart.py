def shopping_cart(*args):
    cart = {'Pizza': [], 'Soup': [], 'Dessert': []}

    for data in args:
        if data == "Stop":
            break
        meal = data[0]
        product = data[1]

        if meal == 'Pizza' and len(cart['Pizza']) == 4:
            continue
        elif meal == 'Soup' and len(cart['Soup']) == 3:
            continue
        elif meal == 'Dessert' and len(cart['Dessert']) == 2:
            continue
        if product not in cart[meal]:
            cart[meal].append(product)

    for ingredients in cart.values():
        if len(ingredients) > 0:
            break
    else:
        return 'No products in the cart!'

    sorted_cart = sorted(cart.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    final_cart = ''

    for meal_type in sorted_cart:
        final_cart += f"{meal_type[0]}:\n"
        sorted_products = sorted(meal_type[1])
        for product in sorted_products:
            final_cart += f" - {product}\n"

    return final_cart


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
