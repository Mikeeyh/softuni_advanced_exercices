def grocery_store(**kwargs):
    sorted_products = sorted(kwargs.items(),
                             key=lambda x: (-x[1], -len(x[0]), x[0]),
                             reverse=False)  # can be used without reversed=False

    result = ""
    for product, quantity in sorted_products:
        result += f"{product}: {quantity}\n"

    return result.strip()  # we can return only the result without strip(), strip() is used to remove all whitespaces


print(grocery_store(bread=5, pasta=12, eggs=12,))
