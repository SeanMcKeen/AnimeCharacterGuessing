import random

class Character():
    def __init__(self, name, hair, quote, anime):
        self.name = name
        self.hair = hair
        self.quote = quote
        self.anime = anime

allCharactersList = []
with open('CharacterList.txt', 'rt') as myFile:
    contents = myFile.read()
characterArray = contents.split('\n')
for char in characterArray:
    character = char.split(' | ')
    allCharactersList.append(Character(character[0], character[1], character[2], character[3]))

while True:
    response = input("Ready to guess a character? ")
    if response.lower() == "yes":
        chosenCharacter = random.choice(allCharactersList)
        print(' ')
        print("This character is from the anime: " + chosenCharacter.anime)
        hintcount = 0
        Playing = True
        characterName = chosenCharacter.name
        while Playing:
            print(' ')
            response = input("Take a guess or say 'hint' if you need another hint! ")
            if response.lower() != "hint":
                if response.lower() in characterName.lower() and len(response.strip()) >= 4:
                    print("Wow! You guessed the character! It was in fact: " + chosenCharacter.name)
                    Playing = False
                else:
                    print("Sorry! This character is incorrect!")
            else:
                hintcount += 1
                if hintcount == 1:
                    print("This character's hair color is: " + chosenCharacter.hair)
                elif hintcount == 2:
                    print("One of this character's quotes from the show is: " + chosenCharacter.quote)
                else:
                    print("Sorry! You used up all of your available hints!")
    elif response.lower() == "no" or response.lower() == "quit" or response.lower() == "exit":
        print("aw man :(")
        break
    else:
        print('Unknown option, did you type it right?')
    print(' ')
