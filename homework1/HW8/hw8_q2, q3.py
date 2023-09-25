"""
Author: [Natanya Anderson]
Assignment / Part: HW8 - Q2, Q3 (depending on the file name)
Date due: 2022-11-17, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

def create_entry (number, name, type_1, type_2, health_points, attack, defense, speed, is_legendary):
    dictionary = {}
    dictionary["Number"] = number
    dictionary["Name"] = name
    if type_2 == "":
        type_2 = None
    dictionary["Types"] = (type_1, type_2)
    dictionary["Battle Stats"] = {}
    dictionary["Battle Stats"]["HP"] = health_points
    dictionary["Battle Stats"]["Attack"] = attack
    dictionary["Battle Stats"]["Defense"] = defense
    dictionary["Battle Stats"]["Speed"] = speed
    dictionary["Legendary"] = is_legendary

    return dictionary

def create_pokedex(pokemon_data):
    poke_dex = {}
    new_lines = pokemon_data.split("/n")
    new_lines = new_lines[1:]
    for line in new_lines:
        pokemon_split = line.split(",")
        answer = create_entry(pokemon_split[0], pokemon_split[1], pokemon_split[2], pokemon_split[3], pokemon_split[5], pokemon_split[6], pokemon_split[7], pokemon_split[10], pokemon_split[12])
        poke_dex[pokemon_split[1]] = answer
    return poke_dex

def main():
    pokedex = create_pokedex(POKEMON_DATA)
    pokemon_key = "Ivysaur"

    if pokemon_key not in pokedex:
        print(f"ERROR: Pokemon {pokemon_key} does not exist!")
    else:
        print(f"PRINTING {pokemon_key}'S INFORMATION....")

    for key in pokedex.keys():
        print(f"{key}: {pokedex[key]}")

main()