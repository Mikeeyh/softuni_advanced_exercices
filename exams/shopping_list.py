def shopping_list(budget, **kwargs):
    my_basket = 0
    result = ''
    initial_budget = budget

    while True:
        if initial_budget < 100:
            break

        for key, value in kwargs.items():
            price = value[0]
            quantity = value[1]
            current_sum = price * quantity

            if current_sum <= budget:
                if my_basket < 5:
                    budget -= current_sum
                    my_basket += 1
                    result += f"You bought {key} for {current_sum:.2f} leva.\n"
                else:
                    break

        return result
    return f"You do not have enough budget."



# print(shopping_list(100,
#                     microwave=(70, 2),
#                     skirts=(15, 4),
#                     coffee=(1.50, 10),))

# print(shopping_list(20,
#                     jeans=(19.99, 1)))

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
