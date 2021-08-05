from art import logo
from random import randint

print(logo)
print("")
print("Welcome to Do-Not-Roll-1 game.\n")
print("")
print("Rules:\n1. Roll a single die, and as long as you don't roll 1, you keep adding the values you get.\n2. Feel lucky? keep rolling.\n3. The moment you roll a 1, you loose and the accumulated total will be shown.")
print("")
print("===================================")
print("Rolling...")
print("")

def roll_the_die():
    repeat = True
    total = 0
    while repeat:
        roll = randint(1, 6)
        if roll == 1:
            print(f"You rolled a {roll}, you loose with a total of {total}!")
            break
        else:    
            print(f"You rolled: {roll}")
            total = total + roll
            print(f"You total is: {total}")
            print("Do you want to roll again? Y/N")
            repeat = "y" in input().lower()        
    else:
        print(f"You finished with a total of {total}. Thank you for playing. Good Bye!")

roll_the_die()