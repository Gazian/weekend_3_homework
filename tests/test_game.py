import unittest

from models.player import Player
from models.rps_game import Game, determine_result, determine_2player_game_result

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("Olivia","rock")
        self.player_2 = Player("Patrick","paper")

    def test_game_player_1_has_name(self):
        self.assertEqual("Olivia",self.player_1.name)

    def test_game_player_2_has_name(self):
        self.assertEqual("Patrick",self.player_2.name)

    def test_game_player_1_has_choice(self):
        self.assertEqual("rock",self.player_1.choice)

    def test_game_player_2_has_choice(self):
        self.assertEqual("paper",self.player_2.choice)

    def test_result_is_draw_rock(self):
        self.assertEqual("The game is a Draw",determine_result("rock","rock"))

    def test_2player_game_result_is_draw_rock(self):
        player_1 = Player("Olivia","rock")
        player_2 = Player("Patrick","rock")
        self.assertEqual("The game is a Draw",determine_2player_game_result(player_1,player_2))

    def test_result_is_draw_paper(self):
        self.assertEqual("The game is a Draw",determine_result("paper","paper"))
    
    def test_2player_game_result_is_draw_paper(self):
        player_1 = Player("Olivia","paper")
        player_2 = Player("Patrick","paper")
        self.assertEqual("The game is a Draw",determine_2player_game_result(player_1,player_2))

    def test_result_is_draw_scissors(self):
        self.assertEqual("The game is a Draw",determine_result("scissors","scissors"))

    def test_2player_game_result_is_draw_scissors(self):
        player_1 = Player("Olivia","scissors")
        player_2 = Player("Patrick","scissors")
        self.assertEqual("The game is a Draw",determine_2player_game_result(player_1,player_2))
    
    def test_Player_1_wins_with_rock(self):
        self.assertEqual("Player 1 wins with rock",determine_result("rock","scissors"))

    def test_2player_game_Player_1_wins_with_rock(self):
        player_1 = Player("Olivia","rock")
        player_2 = Player("Patrick","scissors")
        self.assertEqual("Olivia wins with rock",determine_2player_game_result(player_1,player_2))
    
    def test_Player_2_wins_with_rock(self):
        self.assertEqual("Player 2 wins with rock",determine_result("scissors","rock"))

    def test_2player_game_Player_2_wins_with_rock(self):
        player_1 = Player("Olivia","scissors")
        player_2 = Player("Patrick","rock")
        self.assertEqual("Patrick wins with rock",determine_2player_game_result(player_1,player_2))
    
    def test_Player_1_wins_with_paper(self):
        self.assertEqual("Player 1 wins with paper",determine_result("paper","rock"))

    def test_2player_game_Player_1_wins_with_paper(self):
        player_1 = Player("Olivia","paper")
        player_2 = Player("Patrick","rock")
        self.assertEqual("Olivia wins with paper",determine_2player_game_result(player_1,player_2))
    
    def test_Player_2_wins_with_paper(self):
        self.assertEqual("Player 2 wins with paper",determine_result("rock","paper"))
    
    def test_2player_game_Player_2_wins_with_paper(self):
        player_1 = Player("Olivia","rock")
        player_2 = Player("Patrick","paper")
        self.assertEqual("Patrick wins with paper",determine_2player_game_result(player_1,player_2))
    
    def test_Player_1_wins_with_scissors(self):
        self.assertEqual("Player 1 wins with scissors",determine_result("scissors","paper"))

    def test_2player_game_Player_1_wins_with_scissors(self):
        player_1 = Player("Olivia","scissors")
        player_2 = Player("Patrick","paper")
        self.assertEqual("Olivia wins with scissors",determine_2player_game_result(player_1,player_2))
    
    def test_Player_2_wins_with_scissors(self):
        self.assertEqual("Player 2 wins with scissors",determine_result("paper","scissors"))

    def test_2player_game_Player_2_wins_with_scissors(self):
        player_1 = Player("Olivia","paper")
        player_2 = Player("Patrick","scissors")
        self.assertEqual("Patrick wins with scissors",determine_2player_game_result(player_1,player_2))
    
    
