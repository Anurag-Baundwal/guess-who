characters = []

while True:
    name = input("Enter character's name (or 'done' to finish): ")
    if name.lower() == 'done':
        break

    nose = input("Enter nose size (big/small): ")
    hat = input("Does the character wear a hat? (yes/no): ")
    glasses = input("Does the character wear glasses? (yes/no): ")
    hair_color = input("Enter hair color: ")
    beard = input("Does the character have a beard? (yes/no): ")
    gender = input("Enter the gender of the character (male/female): ")
    bald = input("Is the character bald? (yes/no): ")
    moustache = input("Does the character have a moustache? (yes/no): ")

    character = {"name": name, "nose": nose, "hat": hat, "glasses": glasses, "hair_color": hair_color, "beard": beard, "gender": gender, "bald": bald, "moustache": moustache}
    characters.append(character)

print("Character list created: ", characters)
