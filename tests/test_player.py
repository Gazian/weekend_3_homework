import unittest

from models.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.name = "Olivia"
        self.choice = "rock"

    def test_player_has_name(self):
        self.assertEqual("Olivia",self.name)

    def test_player_has_choice(self):
        self.assertEqual("rock",self.choice)



