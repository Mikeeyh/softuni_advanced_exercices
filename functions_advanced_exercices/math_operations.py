def math_operations(*args, **kwargs):
    for i in range(len(args)):
        if i % 4 == 0:
            kwargs['a'] += args[i]
        elif i % 4 == 1:
            kwargs['s'] -= args[i]
        elif i % 4 == 2:
            if not args[i] == 0:
                kwargs['d'] /= args[i]
        elif i % 4 == 3:
            kwargs['m'] *= args[i]

    result = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    final_result = []

    for key, value in result:
        final_result.append(f"{key}:{value:.1f}")

    return '\n'.join(final_result)


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7,d=33, m=15))

# OR ----------------------------------------------------------------------------


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