import os

files = {}

directory = '../'

for element in os.listdir(directory):  # listdir returns a list with directory's content
    f = os.path.join(directory, element)

    if os.path.isfile(f):
        ext = element.split('.')[-1]  # every file has '.' (example.py -> example + py)
        if ext not in files:
            files[ext] = []
        files[ext].append(element)

    else:

        for el in os.listdir(f):
            file_name = os.path.join(f, el)

            if os.path.isfile(file_name):
                ext = el.split('.')[-1]
                if ext not in files:
                    files[ext] = []
                files[ext].append(el)

with open(os.path.join(directory, 'report.txt'), 'w') as output_file:
    for ext, f_names in sorted(files.items()):
        output_file.write(f".{ext}\n")
        for f_name in sorted(f_names):
            output_file.write(f"- - - {f_name}\n")

with open(os.path.join(directory, 'report.txt'), 'r') as result:
    for line in result.readlines():
        print(line, end="")


for ext, file_list in files.items():
    print(f"Extension: .{ext}")
    print(f"Files: {', '.join(file_list)}")
