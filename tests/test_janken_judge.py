import sys
import os

project_root = (os.path.dirname(os.path.dirname(__file__)))
sys.path.append(project_root)

from source import janken_judge

import unittest
# from unittest.mock import patch

class Test_janken_judge(unittest.TestCase):
    def test_win(self):
        patterns = [('チョキ', 'グー'), ('パー', 'チョキ'), ('グー', 'パー')]
        for computer, player in patterns:
            self.assertEqual(janken_judge.judge(computer, player), 'player_win')
            
    def test_lose(self):
        patterns = [('グー', 'チョキ'), ('チョキ', 'パー'), ('パー', 'グー')]
        for computer, player in patterns:
            self.assertEqual(janken_judge.judge(computer, player), 'computer_win')
    
    def test_draw(self):
        patterns = [('グー', 'グー'), ('チョキ', 'チョキ'), ('パー', 'パー')]
        for computer, player in patterns:
            self.assertEqual(janken_judge.judge(computer, player), 'draw')