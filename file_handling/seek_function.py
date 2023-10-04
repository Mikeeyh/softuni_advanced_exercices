with open("seek.txt", "r") as file:
    print(file.read())
    file.seek(0)
    print(file.read())

# seek returns the cursor at the position given
# we have 1 2 3 then we put seek(0) and it returns to the start position
