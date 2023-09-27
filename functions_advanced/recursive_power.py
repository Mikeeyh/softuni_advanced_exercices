def recursive_power(number, power):
    if power == 1:  # 1 because this is the last possible power, if we have 0 it will give us 1
        return number
    return number * recursive_power(number, power - 1)


print(recursive_power(2, 10))
print(recursive_power(10, 100))

# OR -------------------------------------------------------------------------------------------


def recursive_power(number, power):
    # Base case: If the power is 0, return 1
    if power == 0:
        return 1
    # Recursive case: Multiply number by itself recursively (power - 1) times
    return number * recursive_power(number, power - 1)


# Example usage:
result = recursive_power(2, 3)  # Calculates 2^3
print(result)  # Output: 8
