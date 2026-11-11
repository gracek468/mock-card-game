import unittest
from unittest.mock import patch
from card_game.communication.ConsoleInOut import *
from card_game.card.entity.Deck import *
from card_game.Game import *
from card_game.LoadCSV import *

class test_task(unittest.TestCase):

    @patch('card_game.communication.ConsoleInOut.get_string')
    def test_get_input_integer(self, mock_get_string):
        #Sub-task 1: Mock Console Input Integer

        mock_get_string.return_value = "18"
        self.assertEqual(get_input_integer(mock_get_string()), 18)

    @patch('card_game.communication.ConsoleInOut.get_string')
    def test_get_game_info(self, mock_get_string):
        #Sub-task 2 – Mock Console Game Info
        
        mock_get_string.side_effect = ["Derek", 3]
        name, num = get_game_info()
        self.assertEqual(num, 3)
        #get_game_info returns both the values so I don't understand how the return value is just meant to be the interger 3

    @patch('card_game.communication.ConsoleInOut.get_string')
    def test_get_integer_max_attempts(self, mock_get_string):
        #Sub-task 3 – Mock Console Input With Built In
        
        mock_get_string.return_value = "abc"
        (get_integer())

        self.assert_any_call(5, get_string)

    def test_get_csv_rows(self):
        #Sub-task 4 – Mock File Load
        pass

    def test_play_a_card_from_deck_random(self):
        #Sub-task 5 – Mock Get Player Names
        pass