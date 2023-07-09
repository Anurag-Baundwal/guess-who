import json
import random

# Load character data from a file
with open('characters.json', 'r') as f:
    characters = json.load(f)

# def best_question(possible_characters, possible_attributes):
    # best_attribute = None
    # best_balance = float('inf')  # Start with infinity, so any balance will be better

    # for attribute, values in possible_attributes.items():
    #     if len(values) == 1:
    #         continue

    #     most_common_value = max(set(values), key = values.count)
    #     count_most_common = values.count(most_common_value)
    #     balance = abs(len(possible_characters) / 2 - count_most_common)

    #     if balance < best_balance:
    #         best_attribute = attribute
    #         best_balance = balance

    # if best_attribute is None:
    #     return None, None

    # return best_attribute, max(set(possible_attributes[best_attribute]), key = possible_attributes[best_attribute].count)

def best_question(possible_characters, possible_attributes):
    best_attribute = None
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
        counts = [values.count(value) for value in distinct_values]

        # Find the value that, if asked, would result in the closest to an even split
        best_value_for_attribute = distinct_values[counts.index(min(counts, key=lambda count: abs(len(possible_characters) / 2 - count)))]

        # Calculate the balance for this value
        balance = abs(len(possible_characters) / 2 - counts[distinct_values.index(best_value_for_attribute)])

        # If this balance is the best so far, update best_attribute and best_value
        if balance < best_balance:
            best_attribute = attribute
            best_value = best_value_for_attribute
            best_balance = balance

    return best_attribute, best_value




def ask_question(character, attribute, expected_answer):
    if character[attribute] == expected_answer:
        return True
    else:
        return False

def play_game():
    mode = input(f'Select mode (bot_vs_bot / vs_human): ')
    print(f"\n#########################\n Selected Mode: {mode}\n#########################\n")
    player1_character = random.choice(characters)
    player2_character = random.choice(characters)

    possible_characters = characters.copy()
    
    # If the game is played against a human, remove the bot's character from the possible characters
    if mode == 'vs_human':
        bot_character_name = input("Enter the name of your character: ")
        for character in possible_characters:
            if character['name'].lower() == bot_character_name.lower():
                possible_characters.remove(character)
                break
            
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

    while len(possible_characters) > 1:
        question, answer = best_question(possible_characters, possible_attributes)

        if question is None:
            break

        print(f"The best question is about '{question}', expecting '{answer}'")

        #bot vs bot
        if mode == 'bot_vs_bot':
            actual_answer = player2_character[question]
            #################################################################
            if actual_answer == answer:
                print("Yes")
                possible_characters = [character for character in possible_characters if character[question] == answer]
            else:
                print("No")
                possible_characters = [character for character in possible_characters if character[question] != answer]

        else:
        #vs human
            opponent_response = input(f"Enter the opponent's response (yes / no): ")
            if opponent_response.lower() == 'yes':
                possible_characters = [character for character in possible_characters if character[question] == answer]
            else:
                possible_characters = [character for character in possible_characters if character[question] != answer]


        ###########################################################################################
        # if ask_question(player2_character, question, answer):
        #     print("Yes")
        #     possible_characters = [character for character in possible_characters if character[question] == answer]
        #     if question == 'bald' and answer == 'yes':
        #         possible_characters = [character for character in possible_characters if character['gender'] == 'male']
        #     possible_attributes[question].remove(answer)
        # else:
        #     print("No")
        #     possible_characters = [character for character in possible_characters if character[question] != answer]
        #     # possible_attributes[question].remove(answer)
        #     possible_attributes[question].remove(actual_answer)

        print(f"Remaining possibilities: {len(possible_characters)}\n")
        
    guess = possible_characters[0]["name"]
    print(f"Guessing the character's name: {guess}")

    # if guess == player2_character["name"]:
    #     print("You win!")
    # else:
    #     print("You lost!")
play_game()
