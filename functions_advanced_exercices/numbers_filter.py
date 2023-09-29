def even_odd_filter(**kwargs):
    for key, value in kwargs.items():
        if key == "even":
            kwargs[key] = [x for x in value if x % 2 == 0]
        elif key == "odd":
            kwargs[key] = [x for x in value if x % 2 != 0]

    return dict(sorted(kwargs.items(), key=lambda kvp: -len(kvp[1])))


print(even_odd_filter(odd=[1, 2, 3, 4, 10, 5], even=[3, 4, 5, 7, 10, 2, 5, 5, 2],))

# OR ------------------------------------------------------------------------------------------------


def even_odd_filter(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if key == "even":
            result[key] = [num for num in value if num % 2 == 0]
        elif key == "odd":
            result[key] = [num for num in value if num % 2 != 0]

    sorted_result = sorted(result.items(), key=lambda item: len(item[1]), reverse=True)

    return dict(sorted_result)


print(even_odd_filter(odd=[1, 2, 3, 4, 10, 5], even=[3, 4, 5, 7, 10, 2, 5, 5, 2],))
