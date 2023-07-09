import json
import random
from itertools import product

# Load character data from a file
with open('characters.json', 'r') as f:
    characters = json.load(f)

def best_question(possible_characters, possible_attributes):
    best_attribute = None
    best_condition = None
    best_balance = float('inf')  # Start with infinity, so any balance will be better

    for attribute in possible_attributes:
        # Get all values for this attribute in possible_characters
        values = [character[attribute] for character in possible_characters]

        # Get only distinct values
        distinct_values = list(set(values))

        # If there's only one distinct value, there's no point in asking about it
        if len(distinct_values) == 1:
            continue

        # Count how many characters have each distinct value
        counts = {value: values.count(value) for value in distinct_values}

        for condition in ['either', 'both']:
            # Calculate balances for each distinct value
            balances = {value: abs(sum([count for val, count in counts.items() if val == value]) - sum([count for val, count in counts.items() if val != value])) for value in distinct_values}

            # Find the value that, if asked, would result in the closest to an even split
            best_value_for_attribute = min(balances, key=balances.get)

            # Calculate the balance for this value
            balance = balances[best_value_for_attribute]

            # If this balance is the best so far, update best_attribute and best_value
            if balance < best_balance:
                best_attribute = attribute
                best_value = best_value_for_attribute
                best_balance = balance
                best_condition = condition

    return best_attribute, best_value, best_condition

def play_game():
    mode = input(f'Select mode (bot_vs_bot / vs_human): ')
    print(f"\n#########################\n Selected Mode: {mode}\n#########################\n")

    player1_characters = [random.choice(characters) for _ in range(2)]
    player2_characters = [random.choice(characters) for _ in range(2)]
    possible_characters = characters.copy()
    
    if mode == "vs_human":
        your_character_name = input("Enter the name of your characters (separated by comma): ")
        your_character_names = your_character_name.split(",")
        possible_characters = [character for character in possible_characters if character['name'] not in your_character_names]

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
        
    while len(possible_characters) > 2:
        question, answer, condition = best_question(possible_characters, possible_attributes)

        if question is None:
            break

        print(f"The best question is 'Do {condition} of your characters have '{question}'?', expecting '{answer}'")

        if mode == 'bot_vs_bot':
            actual_answers = [character[question] for character in player2_characters]

            if condition == 'either':
                if any(answer == actual_answer for actual_answer in actual_answers):
                    print("Yes")
                    possible_characters = [character for character in possible_characters if character[question] == answer]
                else:
                    print("No")
                    # If neither of the opponent's characters has the attribute, we can safely eliminate characters with that attribute.
                    possible_characters = [character for character in possible_characters if character[question] != answer]
            elif condition == 'both':
                if all(answer == actual_answer for actual_answer in actual_answers):
                    print("Yes")
                    # If both of the opponent's characters has the attribute, we can safely eliminate characters without that attribute.
                    possible_characters = [character for character in possible_characters if character[question] == answer]
            else:
                print("No")
                # If not both of the opponent's characters has the attribute, we can't really eliminate any characters based on this information.
        
        # same modification for vs_human mode
        else:
            opponent_response = input(f"Enter the opponent's response (yes / no): ")
            if opponent_response.lower() == 'yes':
                possible_characters = [character for character in possible_characters if character[question] == answer]
            else:
                possible_characters = [character for character in possible_characters if character[question] != answer]

        print(f"Remaining possibilities: {len(possible_characters)}\n")
        
    # guesses = [character["name"] for character in random.sample(possible_characters, 2)]
    if len(possible_characters) >= 2:
        guesses = [character["name"] for character in random.sample(possible_characters, 2)]
    else:
        guesses = [character["name"] for character in possible_characters]

    print(f"Guessing the characters' names: {', '.join(guesses)}")

play_game()
