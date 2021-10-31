from models.player import *

# player_1 = Player("Olivia","rock")
# player_2 = Player("Patrick","paper")

# def get_players_choices(player_1,player_2):
#     player_1 = Player.choice
#     player_2 = Player.choice

def determine_result(choice_1,choice_2):
    if choice_1 == choice_2:
        result = "The game is a Draw"
    elif choice_1 == "rock" and choice_2 == "scissors":
        result = "Player 1 wins with rock"
    elif choice_1 == "scissors" and choice_2 == "rock":
        result = "Player 2 wins with rock"
    elif choice_1 == "paper" and choice_2 == "rock":
        result = "Player 1 wins with paper"
    elif choice_1 == "rock" and choice_2 == "paper":
        result = "Player 2 wins with paper"
    elif choice_1 == "scissors" and choice_2 == "paper":
        result = "Player 1 wins with scissors"
    elif choice_1 == "paper" and choice_2 == "scissors":
        result = "Player 2 wins with scissors"
    return result
    
