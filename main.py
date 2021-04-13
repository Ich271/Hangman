from _ast import keyword
import random

start = input(keyword("Start"))

def generateRandomWord():
    with open("deutsch.txt") as wList:
        wLIstRead = wList.read().split("\n")
        listLengh = len(wLIstRead)
        ran = random.randint(1, listLengh)
        word = wLIstRead[ran]
        return word

word = generateRandomWord()
print(word)

################################################
letters = list(word)
spaces = ["_"] * len(letters)
print(spaces)

while True:
    letter = input("ur guess! >>> ")

    if letter in letters:
        for i in range(len(letters)):
            if letters[i] == letter:
                spaces[i] = letter

        print(spaces)

    if "_" not in spaces:
        print("U won!")
        break
