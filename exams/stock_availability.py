def stock_availability(flavours, command, *args):
    if command == 'delivery':
        for flavour in args:
            flavours.append(flavour)
    elif command == 'sell':
        if args:
            if isinstance(args[0], int):
                for i in range(args[0]):
                    if flavours:
                        flavours.pop(0)
            else:
                for item in args:
                    if item in flavours:
                        flavours = [x for x in flavours if x != item]
        else:
            flavours.pop(0)

    return flavours


# print(stock_availability(
#     ["choco", "vanilla", "banana"],
#     "delivery", "caramel", "berry"))
#
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))

print(stock_availability(["cookie", "chocolate", "banana"], "sell"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
