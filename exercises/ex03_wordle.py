"""Final Wordle Exercise!"""
__author__ = "730477496"
GREEN_BOX: str = "\U0001F7E9"
GRAY_BOX: str = "\U00002B1C"
YELLOW_BOX: str = "\U0001F7E8"
BOXES = ""  
i: int = 0
def contains_char(word: str, wordchar: str) -> bool:
    """search the input word for matching letters with characters"""
    n: int = len(word)
    j: int = 0
    assert len(wordchar) == 1
    while j < n:
        if word[j] == wordchar:
            j += 1
            return True
        else :
            if word[j] != wordchar:
                j += 1
            else :
                return False 
def emojified(guess: str, secret: str) -> str:
    """Codifies strings in emoji colors""" 
    assert len(guess) == len(secret)
    i: int = 0
    BOXES = ""
    while i < len(guess):
        if guess[i] == secret[i]:
            BOXES += GREEN_BOX
        elif contains_char(secret, guess[i]):
            BOXES += YELLOW_BOX
        else : 
            BOXES += GRAY_BOX
        i += 1 
    return BOXES 
def input_guess(length:int) -> str:
    """giving an integer "expected" length of a guess"""
    guess = input("Enter a " + str(length) + " character word: ")
    while len(guess) != length:
        guess = input("That wasn't " + str(length) + " chars! Try again: ")
    return (guess)
def main() -> None:
    """Entry point to the main game and loop"""
    secret = "codes"
    BOXES = "" 
    i: int = 1
    while i < 7:
        print("=== Turn " + str(i) +"/6 ===")
        BOXES = emojified(input_guess(5), secret)
        print(BOXES)
        if BOXES == (GREEN_BOX * 5):
            print("You won in " + str(i) + "/6 turns!")
            return
        i = i + 1
    if i == 7 :
        print("X/6 - Sorry, try again tomorrow!")
if __name__ == "__main__":
    main()
