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

# OR -----------------------------------------------------------------------


def age_assignment(*names, **ages):
    result = []
    for name in names:
        first_letter = name[0]
        if first_letter in ages:
            age = ages[first_letter]
            result.append(f"{name} is {age} years old.")
    result.sort()
    return "\n".join(result)


# Example usage:
print(age_assignment("Alice", "Bob", "Charlie", A=30, B=25, C=35))

