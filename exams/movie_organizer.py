def movie_organizer(*args):
    movie_dict = {}
    sorted_result = ''
    for data in args:
        if data[1] not in movie_dict.keys():
            movie_dict[data[1]] = []
        movie_dict[data[1]].append(data[0])

    sorted_dict = sorted(movie_dict.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    for pair in sorted_dict:
        current_type = pair[0]
        list_of_objects = pair[1]
        sorted_list_of_objects = sorted(list_of_objects)
        sorted_result += f"{current_type} - {len(list_of_objects)}\n"
        for el in sorted_list_of_objects:
            sorted_result += f"* {el}\n"

    return sorted_result


print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))
