import sys
import os

project_root = (os.path.dirname(os.path.dirname(__file__)))
sys.path.append(project_root)

from source import computer

import unittest
from unittest.mock import patch
class TestComputer(unittest.TestCase):
    @patch('random.choice')
    def test_computerfirst_(self, mock_choice):
        mock_choice.return_value = 'グー'
        self.assertEqual(computer.computer_pon(), 'グー')
        
    @patch('random.choice')
    def test_computer_second(self, mock_choice):
        mock_choice.return_value = 'チョキ'
        self.assertEqual(computer.computer_pon(), 'チョキ')
        
    @patch('random.choice')
    def test_computer_third(self, mock_choice):
        mock_choice.return_value = 'パー'
        self.assertEqual(computer.computer_pon(), 'パー')
        
        
    