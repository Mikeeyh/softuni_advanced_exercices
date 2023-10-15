def list_manipulator(numbers, *args):
    my_list = []
    if args[0] == 'add' and args[1] == 'beginning':
        for num in args[2:]:
            my_list.append(num)
        my_list += numbers
    elif args[0] == 'add' and args[1] == 'end':
        my_list = numbers
        for num in args[2:]:
            my_list.append(num)
            
    elif args[0] == 'remove' and args[1] == 'beginning':
        if not args[2:]:
            numbers.pop(0)
            my_list = numbers
        else:
            counter = args[2]
            for i in range(counter):
                numbers.pop(0)
            my_list = numbers

    elif args[0] == 'remove' and args[1] == 'end':
        if not args[2:]:
            numbers.pop(-1)
            my_list = numbers
        else:
            counter = args[2]
            for i in range(counter):
                numbers.pop(-1)
            my_list = numbers

    return my_list


print(list_manipulator([1, 2, 3], 'remove', 'end', 2))
