__author__ = "730477496"

secretword = "python"

Word: str = input("What is your 6-letter guess? ")
correct = "\U0001F7E9"
correctletter = "\U0001F7E8"
incorrect = "\U00002B1C"

if Word == secretword:
    print("Woo! You got it!")
    print("\U0001F7E9" + "\U0001F7E9" + "\U0001F7E9" + "\U0001F7E9" + "\U0001F7E9" + "\U0001F7E9")

emojis = ""

while Word != secretword:
    if len(Word) != 6: 
        Word: str = input("That was not 6 letters! Try again: ")
    if Word == secretword:
        print("Woo! You got it!")
        print("\U0001F7E9" + "\U0001F7E9" + "\U0001F7E9" + "\U0001F7E9" + "\U0001F7E9" + "\U0001F7E9")
        exit
    else: 
        print("Not quite. Play again soon!") 
        'a' 
        if Word[0] == secretword : 
            emojis += ("\U0001F7E9")
        elif Word[0] in secretword : 
            emojis += ("\U0001F7E8")
        else : 
            emojis += ("\U00002B1C") 
        
        if Word[1] == secretword : 
            emojis += ("\U0001F7E9")
        elif Word[1] in secretword : 
            emojis += ("\U0001F7E8")
        else : 
            emojis += ("\U00002B1C") 

        if Word[2] == secretword : 
            emojis += ("\U0001F7E9")
        elif Word[2] in secretword : 
            emojis += ("\U0001F7E8")
        else : 
            emojis += ("\U00002B1C") 

        if Word[3] == secretword : 
            emojis += ("\U0001F7E9")
        elif Word[3] in secretword : 
            emojis += ("\U0001F7E8")
        else : 
            emojis += ("\U00002B1C") 

        if Word[4] == secretword : 
            emojis += ("\U0001F7E9")
        elif Word[4] in secretword : 
            emojis += ("\U0001F7E8")
        else : 
            emojis += ("\U00002B1C") 

        if Word[5] == secretword : 
            emojis += ("\U0001F7E9") 
        elif Word[5] in secretword : 
            emojis += ("\U0001F7E8")
        else : 
            emojis += ("\U00002B1C") 
        print(emojis)
        break 
    