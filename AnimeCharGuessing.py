import random
import os
import time

class Character():
    def __init__(self, name, hair, alignment, quote, anime):
        self.name = name
        self.hair = hair
        self.alignment = alignment
        self.quote = quote
        self.anime = anime

allCharactersList = []
with open('CharacterList.txt', 'rt') as myFile:
    contents = myFile.read()
characterArray = contents.split('\n')
for char in characterArray:
    character = char.split(' | ')
    allCharactersList.append(Character(character[0], character[1], character[2], character[3], character[4]))

while True:
    os.system('cls')
    response = input("Ready to guess a character? ")
    if response.lower() == "yes":
        chosenCharacter = random.choice(allCharactersList)
        print(' ')
        print("This character is from the anime: " + chosenCharacter.anime)
        hintcount = 0
        Playing = True
        characterName = chosenCharacter.name
        keepGoing = False
        while Playing:
            print(' ')
            response = input("Take a guess or say 'hint' if you need another hint! ")
            if response.lower() != "hint":
                if response.lower() in characterName.lower() and len(response.strip()) >= 4:
                    print("Wow! You guessed the character! It was in fact: " + chosenCharacter.name)
                    Playing = False
                else:
                    print("Sorry! This character is incorrect or you didn't type enough of their name! Minimum of 4 characters!")
            else:
                hintcount += 1
                if hintcount == 1:
                    print("This character's hair color is: " + chosenCharacter.hair)
                elif hintcount == 2:
                    print("The characters role, alignment/affiliation, or job in the show is: " + chosenCharacter.alignment)
                elif hintcount == 3:
                    print("This is your last hint! One of this character's quotes from the show is: " + chosenCharacter.quote)
                else:
                    print("Sorry! You used up all of your available hints!")
                    if not keepGoing:
                        doesGiveUp = input("If you give up please type: 'fold', if you want to keep guessing please type: 'continue'... ")
                        if doesGiveUp == "fold":
                            print("Better luck next time! The character was: " + chosenCharacter.name)
                            Playing = False
                        else:
                            keepGoing = True
    elif response.lower() == "no" or response.lower() == "quit" or response.lower() == "exit":
        print("aw man :(")
        break
    else:
        print('Unknown option, did you type it right?')
    print(' ')
    time.sleep(3)
