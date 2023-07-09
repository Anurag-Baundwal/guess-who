import json

# Load character data from a file
with open('characters.json', 'r') as f:
    characters = json.load(f)
    
def print_character_details():
    details = {
        'nose': ['big', 'small'],
        'hat': ['yes', 'no'],
        'glasses': ['yes', 'no'],
        'hair_color': ['black', 'brown', 'white', 'golden', 'red'],
        'beard': ['yes', 'no'],
        'gender': ['male', 'female'],
        'bald': ['yes', 'no'],
        'moustache': ['yes', 'no'],
        'skin_color': ['white', 'black'],
        'eye_color': ['blue', 'brown']
    }

    for attribute, possible_values in details.items():
        print(attribute.capitalize() + ":")
        for value in possible_values:
            count = sum(character[attribute] == value for character in characters)
            print(f"People with {value} {attribute}: {count}")
        print()

print_character_details()
