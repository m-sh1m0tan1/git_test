import sys
import os

project_root = (os.path.dirname(os.path.dirname(__file__)))
sys.path.append(project_root)

from source import player

import unittest
from unittest.mock import patch

class TestPlayer(unittest.TestCase):
    @patch('builtins.input', return_value = '1')
    def test_imput_first(self, mock_imput):
        self.assertEqual(player.player_pon(), 'グー')
        
    @patch('builtins.input', return_value = '2')
    def test_imput_second(self, mock_imput):
        self.assertEqual(player.player_pon(), 'チョキ')
        
    @patch('builtins.input', return_value = '3')
    def test_imput_third(self, mock_imput):
        self.assertEqual(player.player_pon(), 'パー')
        
    @patch('builtins.input', side_effect = ('0', '2'))
    def test_imput_error(self, mock_imput):
        self.assertEqual(player.player_pon(), 'チョキ')