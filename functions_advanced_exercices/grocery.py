def grocery_store(**kwargs):
    sorted_products = sorted(kwargs.items(),
                             key=lambda x: (-x[1], -len(x[0]), x[0]),
                             reverse=False)  # can be used without reversed=False

    result = ""
    for product, quantity in sorted_products:
        result += f"{product}: {quantity}\n"

    return result.strip()  # we can return only the result without strip(), strip() is used to remove all whitespaces


print(grocery_store(bread=5, pasta=12, eggs=12,))

# -x[1] -> sort by quantity in descending order
# -len(x[0]) -> sort by name's length in descending order
# x[0] -> sort by name in ascending order

# OR ------------------------------------------------------------------------------------


def grocery_store(**kwargs):
    sorted_products = dict(sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
    result = []
    for product, quantity in sorted_products.items():
        result.append(f"{product}: {quantity}")

    return "\n".join(result)


print(grocery_store(bread=5, pasta=12, eggs=12,))
