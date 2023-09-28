from functools import reduce


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

# OR -------------------------------------------------------------------


def operate(sign, *args):
    def add():
        return reduce(lambda a, b: a+b, args)

    def subtract():
        return reduce(lambda a, b: a-b, args)

    def multiply():
        return reduce(lambda a, b: a*b, args)

    def divide():
        return reduce(lambda a, b: a/b, args)

    if sign == "+":
        return add()
    elif sign == "-":
        return subtract()
    elif sign == "*":
        return multiply()
    elif sign == "/":
        return divide()


print(operate('/', 1, 2, 3))


# OR ------------------------------------------------------------------------

def operate(sign, *args):
    return reduce(lambda a, b: eval(f"{a}{sign}{b}"), args)


print(operate('/', 1, 2, 3))
