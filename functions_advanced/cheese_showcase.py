def sorting_cheeses(**kwargs):
    for key, value in kwargs.items():
        print(key)
        [print(curr) for curr in sorted(value, reverse=True)]
    return kwargs


sorting_cheeses(Parmesan=[102, 120, 135], Camembert=[100, 100, 105, 500, 430], Mozzarella=[50, 125],)
