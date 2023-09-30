word = input()

try:
    times = int(input())
except ValueError:
    print("Variable times must be an integer.")
else:  # else will be executed only if try is ok
    print(word*times)
