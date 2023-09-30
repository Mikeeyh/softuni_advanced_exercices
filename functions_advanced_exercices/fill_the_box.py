def fill_the_box(height, length, width, *args):
    box_volume = height * length * width
    total_cubes = 0

    for arg in args:
        if arg == "Finish":
            break
        total_cubes += int(arg)

    if total_cubes <= box_volume:
        free_space = box_volume - total_cubes
        return f"There is free space in the box. You could put {free_space} more cubes."
    else:
        cubes_left = total_cubes - box_volume
        return f"No more free space! You have {cubes_left} more cubes."


result = fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish")
print(result)
