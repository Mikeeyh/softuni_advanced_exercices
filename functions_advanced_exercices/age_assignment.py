def age_assignment(*args, **kwargs):
    names = {}
    result = []

    for name in args:
        first_letter = name[0]
        if name not in names.keys():
            names[name] = 0

        for current_name, current_age in kwargs.items():
            if first_letter in current_name:
                names[name] = current_age

    for given_name, given_age in sorted(names.items()):
        result.append(f"{given_name} is {given_age} years old.")

    return '\n'.join(result)


print(age_assignment('gosho', 'mike', 'paraya', g=20, m=10, p=15))

