# open the json file and change the details of the characters as needed.
import json

# Load existing character data
with open('characters.json', 'r') as f:
    characters = json.load(f)

# Iterate over the characters and add skin color
# for character in characters:
#     print(f"Character: {character['name']}")
#     eye_color = input("Enter the eye color of the character (blue/brown): ")
#     character['eye_color'] = eye_color

# To modify specific characters, you can use their names.
# Let's say you want to modify "Peter" and "Jane".
# First, let's find their indices in the characters list.
names_to_modify = ["David", "Zachary"]
indices_to_modify = [i for i, char in enumerate(characters) if char['name'] in names_to_modify]

for i in indices_to_modify:
    print(f"Modifying details for {characters[i]['name']}")
    characters[i]['nose'] = input("Enter nose size (big/small): ")
    characters[i]['hat'] = input("Does the character wear a hat? (yes/no): ")
    characters[i]['glasses'] = input("Does the character wear glasses? (yes/no): ")
    characters[i]['hair_color'] = input("Enter hair color: ")
    characters[i]['beard'] = input("Does the character have a beard? (yes/no): ")
    characters[i]['gender'] = input("Enter the gender of the character (male/female): ")
    characters[i]['bald'] = input("Is the character bald? (yes/no): ")
    characters[i]['moustache'] = input("Does the character have a moustache? (yes/no): ")
    characters[i]['skin_color'] = input("Enter the skin color of the character (white/black): ")

# Save back to the file
with open('characters.json', 'w') as f:
    json.dump(characters, f)
