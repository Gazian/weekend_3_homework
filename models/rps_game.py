from models.player import Player
  
player_1 = Player("Olivia","scissors")
player_2 = Player("Patrick","paper")

# players = [player_1,player_2]

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

def determine_2player_game_result(player_1,player_2):
    if player_1.choice == player_2.choice:
        result = "The game is a Draw"
    elif player_1.choice == "rock" and player_2.choice == "scissors":
        result = f"{player_1.name} wins with rock"
    elif player_1.choice == "scissors" and player_2.choice == "rock":
        result = f"{player_2.name} wins with rock"
    elif player_1.choice == "paper" and player_2.choice == "rock":
        result = f"{player_1.name} wins with paper"
    elif player_1.choice == "rock" and player_2.choice == "paper":
        result = f"{player_2.name} wins with paper"
    elif player_1.choice == "scissors" and player_2.choice == "paper":
        result = f"{player_1.name} wins with scissors"
    elif player_1.choice == "paper" and player_2.choice == "scissors":
        result = f"{player_2.name} wins with scissors"
    return result
    
