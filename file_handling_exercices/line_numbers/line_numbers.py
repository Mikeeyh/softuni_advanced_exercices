from string import punctuation

with open("line_numbers.txt", "r") as file, open("output.txt", "w") as output_file:
    result = []
    for row, line in enumerate(file, start=1):  # in order to start counting from 1
        letters_count = 0
        punc_count = 0
        for char in line:
            if char.isalpha():
                letters_count += 1
            elif char in punctuation:
                punc_count += 1

        result.append(f"Line {row}: {line[:-1]} ({letters_count})({punc_count})")
    output_file.write('\n'.join(result))
print('\n'.join(result))

# OR -- using strip in order to avoid white spaces after the lines. line.strip() == line[:-1]

with open("line_numbers.txt", "r") as file:
    result = []
    for row, line in enumerate(file):
        letters_count = 0
        punc_count = 0
        for char in line:
            if char.isalpha():
                letters_count += 1
            elif char not in [' ', '\n']:
                punc_count += 1

        result.append(f"Line {row + 1}: {line.strip()} ({letters_count})({punc_count})")
print('\n'.join(result))
