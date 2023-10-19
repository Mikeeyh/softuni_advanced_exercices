def add_songs(*args):
    song_dict = {}
    result = ''
    for data in args:
        current_song_name = data[0]
        song_lyrics = data[1]

        if current_song_name not in song_dict.keys():
            song_dict[current_song_name] = []
        if any(song_lyrics):
            song_dict[current_song_name] += song_lyrics

    for name, current_lyrics in song_dict.items():
        result += f"- {name}\n"
        for el in current_lyrics:
            result += f"{el}\n"

    return result.strip()


print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))

print(add_songs(
    ("Beat It", []),
    ("Beat It",
     ["Just beat it (beat it), beat it (beat it)",
      "No one wants to be defeated"]),
    ("Beat It", []),
    ("Beat It",
     ["Showin' how funky and strong is your fight",
      "It doesn't matter who's wrong or right"]),
))
