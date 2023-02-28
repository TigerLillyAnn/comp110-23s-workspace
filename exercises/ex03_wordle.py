"""Final Wordle Exercise!"""
__author__ = "730477496"
GREEN_BOX: str = "\U0001F7E9"
GRAY_BOX: str = "\U00002B1C"
YELLOW_BOX: str = "\U0001F7E8"
BOXES = ""  
i: int = 0
def contains_char(Str, Char) -> bool:
    """search the input word for matching letters with characters"""
    n: int = len(Str)
    j: int = 0
    assert len(Char) == 1
    while j < n:
        if Str[j] == Char:
            j += 1
            return True
        else :
            if Str[j] != Char:
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
        else:
            j: int = 0
            in_secret: bool = False
            while j < len(guess):
                if guess[j] == secret[i]:
                    in_secret = True
                j += 1
                if in_secret:
                    BOXES += YELLOW_BOX
                else:
                    BOXES += GRAY_BOX
            i = i + 1 
    return(BOXES)
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
    i: int = 0
    while i < 7:
        print("=== Turn " + str(i) +"/6 ===")
        emoji: str = emojified(input_guess(5), secret)
        print(BOXES)
        if BOXES == (GREEN_BOX * 5):
            print("You won in " + str(i) + "/6 turns!")
            return
        i = i + 1
    if i == 7 :
        print("X/6 - Sorry, try again tomorrow!")
if __name__ == "__main__":
    main()

