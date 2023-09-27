def recursive_power(number, power):
    # Base case: If the power is 0, return 1
    if power == 0:
        return 1
    # Recursive case: Multiply number by itself recursively (power - 1) times
    return number * recursive_power(number, power - 1)


# Example usage:
result = recursive_power(2, 3)  # Calculates 2^3
print(result)  # Output: 8
