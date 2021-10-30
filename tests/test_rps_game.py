import unittest
from models.rps_game import Game, determine_result
from models.player import *

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player_1 = "Olivia"
        self.player_1_choice = "rock"
        self.player_2 = "Patrick"
        self.player_2_choice = "paper"

    def test_player_1_has_name(self):
        self.assertEqual("Olivia", self.player_1)

    def test_player_1_has_choice(self):
        self.assertEqual("rock", self.player_1_choice)

    def test_player_2_has_name(self):
        self.assertEqual("Patrick", self.player_2)

    def test_player_2_has_choice(self):
        self.assertEqual("paper", self.player_2_choice)

    def test_result_player_1_wins_with_rock(self):
        player_1_choice = "rock"
        player_2_choice = "paper"
        result = determine_result(player_1_choice,player_2_choice)
        self.assertEqual("Player 1 wins with rock",result)
