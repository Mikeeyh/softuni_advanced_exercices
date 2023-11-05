def team_lineup(*args):
    my_dict = {}
    final_result = []
    for name, country in args:
        if country not in my_dict:
            my_dict[country] = []
        my_dict[country].append(name)

    sorted_dict_data = sorted(my_dict.items(), key=lambda x: (-len(x[1]), x[0], -len(x[0])))

    for given_country, current_list_of_players in sorted_dict_data:
        final_result.append(f"{given_country}:")
        for current_player in current_list_of_players:
            final_result.append(f"  -{current_player}")

    return "\n".join(final_result)

# def team_lineup(*args):
#     # Create a dictionary to store players by country
#     players_by_country = {}
#
#     # Group players by country and count the players per country
#     for name, country in args:
#         if country not in players_by_country:
#             players_by_country[country] = []
#         players_by_country[country].append(name)
#
#     # Sort the countries by the number of players (descending) and then by the country name length (descending)
#     sorted_countries = sorted(players_by_country.items(), key=lambda item: (-len(item[1]), item[0], -len(item[0])))
#
#     result = []
#
#     # Iterate through sorted countries and players
#     for country, players in sorted_countries:
#         result.append(f"{country}:")
#         for player in players:
#             result.append(f"  - {player}")  # Add a space before the player's name
#
#     return "\n".join(result)


print(team_lineup(
    ("Harry Kane", "England"),
    ("Manuel Neuer", "Germany"),
    ("Raheem Sterling", "England"),
    ("Toni Kroos", "Germany"),
    ("Cristiano Ronaldo", "Portugal"),
    ("Thomas Muller", "Germany")
))

# print(team_lineup(
#     ("Lionel Messi", "Argentina"),
#     ("Neymar", "Brazil"),
#     ("Cristiano Ronaldo", "Portugal"),
#     ("Harry Kane", "England"),
#     ("Kylian Mbappe", "France"),
#     ("Raheem Sterling", "England")))