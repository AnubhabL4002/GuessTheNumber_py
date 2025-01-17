import random
from art import logo

def check(the_number, the_guess):
    """It checks if the guess and the number are same."""
    if the_guess < the_number:
        print("********Too Low!********")
        return False
    elif the_guess > the_number:
        print("********Too High!********")
        return False
    else:
        print("\n********You Got It Right!********")
        return True

print(logo)
number=random.randint(1,100)
print("Welcome to Guess The Number Game!\nI'm thinking about a number from 1 to 100.")
difficulty = input("Choose the difficulty -> Type 'easy' or 'hard'")
lives = 10
game_over = False
if difficulty == 'hard':
    lives = 5
while not game_over:
    if lives > 0:
        print(f"Attempts remaining: {lives}.\nMake a guess...")
        guess=int(input())
        lives-=1
        game_over = check(number,guess)
    else:
        print(f"You couldn't guess the number.... It was {number}.\nGame Over!\n")
        break
print("Thank you for Playing! :)")
