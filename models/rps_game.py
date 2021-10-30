from models.player import *

player_1 = Player("Olivia","rock")
player_2 = Player("Patrick","paper")

def determine_result(player_1,player_2):
    if player_1.choice == player_2.choice:
        result = "The game is a Draw"
    elif player_1.choice == "rock" and player_2.choice == "scissors":
        result = "Player 1 wins with rock"
    elif player_1.choice == "scissors" and player_2.choice == "rock":
        result = "Player 2 wins with rock"
    elif player_1.choice == "paper" and player_2.choice == "rock":
        result = "Player 1 wins with paper"
    elif player_1.choice == "rock" and player_2.choice == "paper":
        result = "Player 2 wins with paper"
    elif player_1.choice == "scissors" and player_2.choice == "paper":
        result = "Player 1 wins with scissors"
    elif player_1.choice == "paper" and player_2.choice == "scissors":
        result = "Player 2 wins with scissors"
    
