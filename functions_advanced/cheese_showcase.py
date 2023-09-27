def sorting_cheeses(**kwargs):
    sorted_dict = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    result = ""

    for name, quantities in sorted_dict:
        result += f"{name}\n"  # prints the name then adds new line
        sorted_quantities = sorted(quantities, reverse=True)  # reverse the list in descending order
        result += "\n".join([str(el) for el in sorted_quantities])  # prints each quantity and adds new line after each
        result += "\n"  # prints new line after the last quantity before moving to the other name

    return result

    # We sort by length of the list -> len(kvp)
    # We use [1] to sort by value and not by key -> kvp[1]
    # We add minus because it is a descending order -> -len(kvp[1])
    # We add parentheses because we should sort differently if there are two items with the same length
    # It is called sort by, then by -> (-len(kvp[1]), kvp[0]))


print(sorting_cheeses(Parmesan=[102, 120, 135], Camembert=[100, 100, 105, 500, 430], Mozzarella=[50, 125],))
