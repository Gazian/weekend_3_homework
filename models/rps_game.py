def determine_result(player_1_choice,player_2_choice):
    if player_1_choice == player_2_choice:
        result = "The game is a Draw"
    elif player_1_choice == "rock" and player_2_choice == "scissors":
        result = "Player 1 wins with rock"
    elif player_1_choice == "scissors" and player_2_choice == "rock":
        result = "Player 2 wins with rock"
    elif player_1_choice == "paper" and player_2_choice == "rock":
        result = "Player 1 wins with paper"
    elif player_1_choice == "rock" and player_2_choice == "paper":
        result = "Player 2 wins with paper"
    elif player_1_choice == "scissors" and player_2_choice == "paper":
        result = "Player 1 wins with scissors"
    elif player_1_choice == "paper" and player_2_choice == "scissors":
        result = "Player 2 wins with scissors"
    return result


    
