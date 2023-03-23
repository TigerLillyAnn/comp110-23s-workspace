"""creating a role playing game!"""
___author___ = "730477496"
import random
BOAT: str = "\u2693"
CITY: str = "\U0001F3D9"

def chance_game(points: int) -> int:
    global player
    print("Welcome to the wonderful Game of Chance {player}! You currently have {points} points!")
    print("You are now playing the Game of Chance. Roll the dice to earn points")
    print("1. Roll the dice.")
    print("2. Leave the Game of Chance")
    choice = input("Enter your choice: ")
    if choice == "1":
        roll = random(1,6)
        print(f"You rolled a {roll}")
    elif choice == "2":
        print("You left the Game of Chance.")
    print(f"Your total points are {points}.")
    return points

def greet():
    global player
    print("Welcome to the Game!")
    player = input("What is your name? ")
    print(f"Hello, {player}! Let's begin your Journey.")

def path1():
    print("You chose path 1. This path leads to an ocean shore.") 
    print("You can either go for a swim, or continue along the sea shore.")
    points = 0
    while True:
        print("What shall you do?")
        print("1. Go for a swim. It looks nice after all and you could use a nice dip!")
        print("2. Keep walking along the shore. A walk is always good for your bones.")
        print("3. Return back to start.")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("You went for a swim. As you are enjoying the water, you see a large shadow come up to you.")
            print("What do you do now?")
            print("1. Swim towards the shadow.")
            print("2. Swim back to shore")
            swim_choice = input("Enter your choice: ")
            if swim_choice == "1":
                print("You've made a friend! His name is Jeffery and wishes you well along your journey.")
                points += 20
            else:
                print("You swim away from the shadow and return to the shore.")
        elif choice == "2":
            print("You continue to walk along the shore and see a seagull trying to devor a newly-hatched sea turtle.")
            print("What do you do?")
            print("1. Scare off the seagull.")
            print("2. Let nature take its course.")
            seagull_choice = input("Enter your choice: ")
            if seagull_choice == "1":
                print("You saved the sea turtle. It seems to give you a small wink as it continues its own journey.")
                points += 10
            else:
                print("You continue on your way as two lives become only one.All creatures need to eat afterall.")
        elif choice == "3":
            print("You return back to the start.")
            break
        else:
            print("invalid choice. Please try again.")
    print(f"You earned {points} adventure points on your Ocean Shores exploratoin!")
    global adventure_points 
    adventure_points += points
            
def path2():
    print("You chose path 2. This path leads to the City of Metal. A large and sprawling city full of the advancements of Technology.")
    points = 0
    while True:
        print("1. You see a large market that is full of many bizarre tents and goods in the city square.")
        print("2. You see a dark alley. While it does not seem unfriendly, it is definitely dark.")
        print("3. Return to the start")
        print("Where shall you go?")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("You enter the market. A man walks up to you and askes if you will play a Game of Chance with him.")
            print("1. Yes, lets play.")
            print("2. No. I dont have time for games.")
            print("3. Return to the start")
            game_choice = input("Will you play the game?")
            if game_choice == "1":
                chance_game
                print("The man jumps with glee with the ending of the game.")
                print("Time to continue the adventure")
            elif game_choice == "2":
                print("Fine. I think it would have been fun but its your adventure.")
                points -= 2
            else:
                print("Invalid choice. Pick a valid option.")
        elif choice == "2":
            print("You enter the dark alley.")
            print("From where you stood, it seemed so long and dark. As you get closer, you realize that its very short and nothing lurks in the Alley.")
            print("Brave of you to check, however.")
            points += 5
        elif choice == "3":
            print("You return to the start of the adventure.")
            break
        else:
            print("That is not a valid input. Try again.")
            path2()
            

            



def end_game(adventure_points):
    print(f"Goodbye! You collected {adventure_points} adventure points")

def main():
    greet()
    adventure_points = 0
    while True:
        print("Choose your adventure path")
        print("1. Travel to the Ocean Shore " + BOAT)
        print("2. Travel to the City of Metal " + CITY)
        print("3. End the adventure.")
        choice = input("Enter your choice: ")
        if choice == "1":
            path1()
        elif choice == "2":
            path2()
        elif choice == "3":
            end_game(adventure_points)
        else:
            print("Invalid choice. Try again.")
if __name__ == "__main__":
    main()