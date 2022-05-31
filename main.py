"""
    This is a game of Rock Paper and Scissors
"""
import random

options = ['R', 'P', 'S']
computer = random.choice(options)


while True:

    user = str.upper(input("\nThis is a game of Rock Paper and Scissors, choose your character. \nEnter R for Rock \nEnter P for Paper \nEnter S for Scissors:     "))

    if user in options:
    
        print(f"\nYou {user} : Computer {computer}")

        if computer == user:
            print("\nIt's a draw. Have another go!")
        elif user == 'R':
            #if player picks rock
            if computer == 'S':
                print("You win")
                break
            else:
                print("You lose")
                break
        elif user == 'S':
            #if player picks scissors
            if computer == 'P':
                print("You win")
                break
            else:
                print("You lose")
                break       
        elif user == 'P':
            #if player picks paper
            if computer == 'R':
                print("You win")
                break
            else:
                print("You lose")
                break
    else:
        print("\nPlease enter a letter among the options provided")