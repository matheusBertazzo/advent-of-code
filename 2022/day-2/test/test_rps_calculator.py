import unittest
from src.rps_calculator import calculate

class TestRpsCalculator(unittest.TestCase):
    
    def test_calculator_given_a_game_you_win_with_a_rock(self):        
        result = calculate('C', 'A')
        self.assertEqual(result, 7)

    def test_calculator_given_a_game_you_win_with_a_paper(self):        
        result = calculate('A', 'B')
        self.assertEqual(result, 8)
    
    def test_calculator_given_a_game_you_win_with_a_scissor(self):        
        result = calculate('B', 'C')
        self.assertEqual(result, 9)

    def test_calculator_given_a_game_you_lose_with_a_rock(self):        
        result = calculate('B', 'A')
        self.assertEqual(result, 1)

    def test_calculator_given_a_game_you_lose_with_a_paper(self):        
        result = calculate('C', 'B')
        self.assertEqual(result, 2)
    
    def test_calculator_given_a_game_you_lose_with_a_scissor(self):        
        result = calculate('A', 'C')
        self.assertEqual(result, 3)
    
    def test_calculator_given_a_draw_of_rocks(self):        
        result = calculate('A', 'A')
        self.assertEqual(result, 4)

    def test_calculator_given_a_draw_of_papers(self):        
        result = calculate('B', 'B')
        self.assertEqual(result, 5)
    
    def test_calculator_given_a_draw_of_scissors(self):        
        result = calculate('C', 'C')
        self.assertEqual(result, 6)