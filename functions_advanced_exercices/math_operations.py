def math_operations(*args, **kwargs):
    result_dict = {}
    operations = {"a": "add", "s": "subtract", "d": "divide", "m": "multiply"}

    for i, arg in enumerate(args):
        key = list(kwargs.keys())[i % len(kwargs)]
        value = kwargs[key]

        if operations[key] == "add":
            result = value + arg
        elif operations[key] == "subtract":
            result = value - arg
        elif operations[key] == "divide":
            if arg == 0:
                continue  # Skip division by zero
            result = value / arg
        elif operations[key] == "multiply":
            result = value * arg

        kwargs[key] = result

    sorted_items = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))

    return "\n".join([f"{item[0]}: {item[1]:.1f}" for item in sorted_items])


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7,d=33, m=15))