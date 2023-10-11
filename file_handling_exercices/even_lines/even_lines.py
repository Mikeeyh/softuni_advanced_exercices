with open("even_lines.txt", "r") as file:
    result = ''
    for row, line in enumerate(file.readlines()):  # using enumerate to take each row's index as well
        if row % 2 == 0:
            for char in ["-", ",", ".", "!", "?"]:
                line = line.replace(char, '@')
            print(' '.join(reversed(line.split())))
            