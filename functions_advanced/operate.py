def operate(operator, *args):
    if operator == "+":
        result = sum(args)
    elif operator == "-":
        result = args[0] - sum(args[1:])
    elif operator == "*":
        result = 1
        for num in args:
            result *= num
    elif operator == "/":
        if not 0 in args[1:]:
            result = args[0]
            for num in args[1:]:
                result /= num

    return result


print(operate('/', 1, 2, 3))





