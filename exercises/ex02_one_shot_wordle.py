__author__ = "730477496"

word: str = input("What is your 6-letter guess? ")
while len(word) != len("python"):
    word = input("That was not 6 letters! Try again: ")

if word == "python":
    print("Woo! You got it!")
    print("\U0001F7E9" + "\U0001F7E9" + "\U0001F7E9" + "\U0001F7E9" + "\U0001F7E9" + "\U0001F7E9")
    exit

i = int = 0

while i < len("python"):
    if i == "python" :
        print("\U0001F7E9")
        i = i + 1 
    else:
        if word[i] in "python":
            print("\U0001F7E8")
            i = i + 1
        else:
            print("\U00002B1C")
            i = i + 1
