def start_spring(**kwargs):
    new_objects = {}

    for name, object_type in kwargs.items():
        if object_type not in new_objects:
            new_objects[object_type] = []
        new_objects[object_type].append(name)

    sorted_objects = sorted(new_objects.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    result = ''

    for pair in sorted_objects:
        current_type = pair[0]
        list_of_objects = pair[1]
        sorted_list_of_objects = sorted(list_of_objects)
        result += f"{current_type}:\n"
        for el in sorted_list_of_objects:
            result += f"-{el}\n"

    return result.strip()


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower", }
print(start_spring(**example_objects))
