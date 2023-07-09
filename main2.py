import json
import random

# Load character data from a file
with open('characters.json', 'r') as f:
    characters = json.load(f)

def best_question(possible_characters, possible_attributes):
    best_attribute = None
    best_balance = float('inf')  # Start with infinity, so any balance will be better

    for attribute, values in possible_attributes.items():
        if len(values) == 1:
            continue

        most_common_value = max(set(values), key = values.count)
        count_most_common = values.count(most_common_value)
        balance = abs(len(possible_characters) / 2 - count_most_common)

        if balance < best_balance:
            best_attribute = attribute
            best_balance = balance

    if best_attribute is None:
        return None, None

    return best_attribute, max(set(possible_attributes[best_attribute]), key = possible_attributes[best_attribute].count)

def ask_question(character, attribute, expected_answer):
    if character[attribute] == expected_answer:
        return True
    else:
        return False

def play_game():
    player1_character = random.choice(characters)
    player2_character = random.choice(characters)

    possible_characters = characters.copy()
    possible_attributes = {
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

    while True:
        question, answer = best_question(possible_characters, possible_attributes)

        if question is None:
            guess = possible_characters[0]["name"]
            print(f"Guessing the character's name: {guess}")

            if guess == player2_character["name"]:
                print("You win!")
            else:
                print("You lost!")
            break

        print(f"The best question is about '{question}', expecting '{answer}'")

        if ask_question(player2_character, question, answer):
            print("Yes")
            possible_characters = [character for character in possible_characters if character[question] == answer]
            if question == 'bald' and answer == 'yes':
                possible_characters = [character for character in possible_characters if character['gender'] == 'male']
            possible_attributes[question].remove(answer)
        else:
            print("No")
            possible_characters = [character for character in possible_characters if character[question] != answer]
            possible_attributes[question].remove(answer)

        print(f"Remaining possibilities: {len(possible_characters)}")

play_game()
