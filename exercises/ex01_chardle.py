"""EX01 - Chardle - A cute step towards Wordle!"""
__author__ = 730477496

Word: str = input("Enter a 5-character word:")
if 5 < len(Word) > 5: 
    print("Error: Word must contain 5 letters")
    exit()
Letter: str = input("Enter a single character:")
if 2 < len(Letter) > 2: 
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + Letter + " in " + Word)

x: int = 0

if 5 < len(Word) > 5: 
    print("Error: Word must contain 5 letters")

if (Word[0] == Letter): 
    print(Letter + " found at index 0")
    x = x + 1

if (Word[1] == Letter):
    print(Letter + " found at index 1")
    x = x + 1

if (Word[2] == Letter):
    print(Letter + " found at index 2")
    x = x + 1

if (Word[3] == Letter):
    print(Letter + " found at index 3")
    x = x + 1

if (Word[4] == Letter):
    print(Letter + " found at index 4") 
    x = x + 1 

if (x == 1):
    print(x, "instance of " + Letter + " found in " + Word)

if (x == 0):
    print("No instances of " + Letter + " found in " + Word)

if (x >= 2):
    print(x, "instances of " + Letter + " found in " + Word)
