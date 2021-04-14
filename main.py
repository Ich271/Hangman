import random


def generateRandomWord():
    with open("deutsch.txt") as wList:
        wLIstRead = wList.read().split("\n")
        listLengh = len(wLIstRead)
        ran = random.randint(1, listLengh)
        word = wLIstRead[ran]
        return word


case = {1: " ┌────┐\n o    │\n⁄│\   │\n⁄ \   ┴",
        2: " ┌────┐\n o    │\n⁄│\   │\n⁄     ┴",
        3: " ┌────┐\n o    │\n⁄│\   │\n      ┴",
        4: " ┌────┐\n o    │\n⁄│    │\n      ┴",
        5: " ┌────┐\n o    │\n │    │\n      ┴",
        6: " ┌────┐\n o    │\n      │\n      ┴",
        7: " ┌────┐\n      │\n      │\n      ┴",
        8: "  ────┐\n      │\n      │\n      ┴",
        9: "      ┐\n      │\n      │\n      ┴",
        10: "      \n      │\n      │\n      ┴",
        11: "      \n       \n      │\n      ┴",
        12: "      \n       \n       \n      ┴",
        13: "      \n       \n       \n       ",
        }



word = generateRandomWord()
word = word.lower()

letters = list(word)
spaces = ["_"] * len(letters)
print(spaces)

versuche = 13

while True:
    letter = input("ur guess! >>> ")

    if letter in letters:
        for i in range(len(letters)):
            if letters[i] == letter:
                spaces[i] = letter
    else:
        versuche -= 1
        print(case[versuche])
        if versuche <= 1:
            print("u died")
            exit(0)
    print(spaces)

    if "_" not in spaces:
        print("U won!")
        exit(0)