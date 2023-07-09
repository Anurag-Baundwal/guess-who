import random

characters = [
    {"name": "John", "nose": "big", "hat": "yes", "glasses": "no", "hair_color": "black", "beard": "no"},
    {"name": "Anna", "nose": "small", "hat": "no", "glasses": "yes", "hair_color": "brown", "beard": "no"},
    # add more characters here with different attributes
]

def ask_question(character, question, answer):
    return character[question] == answer

def play_game():
    player1_character = random.choice(characters)
    player2_character = random.choice(characters)

    while True:
        print("Player 1's turn")
        question = input("What is your question? (nose/hat/glasses/hair_color/beard) ")
        answer = input("What is your expected answer? ")
        if ask_question(player2_character, question, answer):
            print("Yes")
        else:
            print("No")

        print("Player 2's turn")
        question = input("What is your question? (nose/hat/glasses/hair_color/beard) ")
        answer = input("What is your expected answer? ")
        if ask_question(player1_character, question, answer):
            print("Yes")
        else:
            print("No")

        guess = input("Player 1, do you want to guess the character? (yes/no) ")
        if guess == "yes":
            name = input("What's the name of the character? ")
            if name == player2_character["name"]:
                print("Player 1 wins!")
                break
            else:
                print("Wrong guess. Continue the game.")

        guess = input("Player 2, do you want to guess the character? (yes/no) ")
        if guess == "yes":
            name = input("What's the name of the character? ")
            if name == player1_character["name"]:
                print("Player 2 wins!")
                break
            else:
                print("Wrong guess. Continue the game.")

play_game()
