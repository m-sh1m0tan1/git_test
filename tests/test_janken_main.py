# import sys
# import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../source')))
# import sys 
# import os 
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'source')))

import unittest
from unittest.mock import patch
from source.janken_main import first, second, third


class Testjankenmain(unittest.TestCase):
    @patch('builtins.input', side_effect = '2')
    @patch('builtins.input', side_effect = '1')
    # @patch('random.choice')
    # @patch('janken_main.first')
    def test_win(self, mock_player_pon, mock_computer_pon):
        # mock_computer_pon.return_value = 'パー'
        result = second(2, 1)
        self.assertEqual(result, 'あなたの総合勝利です！')
        
    @patch('builtins.input', side_effect = '1')
    @patch('builtins.input', side_effect = '2')
    def test_lose(self, mock_player_pon, mock_computer_pon):
        result = second(1, 2)
        self.assertEqual(result, 'コンピュータの総合勝利です！')