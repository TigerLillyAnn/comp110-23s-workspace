"""Super close version of Wordle!!!"""
__author__ = "730477496"

GREEN_BOX: str = "\U0001F7E9"
GRAY_BOX: str = "\U00002B1C"
YELLOW_BOX: str = "\U0001F7E8"
BOXES = ""

secret: str = "python"
word: str = input("What is your 6-letter guess? ")

while len(word) != len(secret):
    word = input("That was not 6 letters! Try again: ")

i: int = 0

while i < len(secret):
    if word[i] == secret[i]:
        BOXES += GREEN_BOX
    else:
        j: int = 0
        in_secret: bool = False
        while j < len(secret):
            if secret[j] == word[i]:
                in_secret = True
            j += 1
        if in_secret:
            BOXES += YELLOW_BOX
        else:
            BOXES += GRAY_BOX
    
    i = i + 1 

print(BOXES)
if word != secret:
    print("Not quite. Play again soon!")

if word == secret:
    print("You got it!")
exit 