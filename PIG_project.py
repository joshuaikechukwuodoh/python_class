""""
import random


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started!")
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)

            print("Your score is:", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1,
      "is the winner with a score of:", max_score)
      """

import random
print("""
 
    _  ____  ____  _     _     ____    ____  _      _  _____  _      
   / |/  _ \/ ___\/ \ /|/ \ /\/  _ \  / ___\/ \__/|/ \/__ __\/ \ /|  
   | || / \||    \| |_||| | ||| / \|  |    \| |\/||| |  / \  | |_||  
/\_| || \_/|\___ || | ||| \_/|| |-||  \___ || |  ||| |  | |  | | ||  
\____/\____/\____/\_/ \|\____/\_/ \|  \____/\_/  \|\_/  \_/  \_/ \|  
                                                                     
 ____  _  _____   _____ ____  _      _____                           
/  __\/ \/  __/  /  __//  _ \/ \__/|/  __/                           
|  \/|| || |  _  | |  _| / \|| |\/|||  \                             
|  __/| || |_//  | |_//| |-||| |  |||  /_                            
\_/   \_/\____\  \____\\_/ \|\_/  \|\____\                           
                                                                     

""")


name = input("enter your username:").capitalize()

print(f"WELCOME TO PIG GAME: {name}")

# value = Roll just remember that ok
def roll():
    max_value = 6
    min_value = 1
    roll = random.randint(min_value,max_value)
    return roll
value = roll()
print(value)

score = 0



"""while True:
    player = input("Do you want to roll? (y/n):")
    if player == "y":
        print(f"You roll is :{value}")
        player_score = score =+ value
        print(f"Your score is :{player_score}")
        
        continue
    else:
        print("it is ok to roll ,thank you!")"""