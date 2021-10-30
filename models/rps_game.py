class Game:

    def __init__(self,player_1,player_1_choice,player_2,player_2_choice):
        self.player_1 = player_1
        self.player_1_choice = player_1_choice
        self.player_2 = player_2
        self.player_2_choice = player_2_choice

    def determine_result(self,player_1_choice,player_2_choice):
        if player_1_choice == player_2_choice:
            result = "The game is a Draw"
        elif player_1_choice == "rock" and player_2_choice == "scissors":
            result = f"Player 1 wins with {player_1_choice}"
        elif player_1_choice == "scissors" and player_2_choice == "rock":
            result = f"Player 2 wins with {player_2_choice}"
        elif player_1_choice == "paper" and player_2_choice == "rock":
            result = f"Player 1 wins with {player_1_choice}"
        elif player_1_choice == "rock" and player_2_choice == "paper":
            result = f"Player 2 wins with {player_2_choice}"
        elif player_1_choice == "scissors" and player_2_choice == "paper":
            result = f"Player 1 wins with {player_1_choice}"
        elif player_1_choice == "paper" and player_2_choice == "scissors":
            result = f"Player 2 wins with {player_2_choice}"
        return result


    
