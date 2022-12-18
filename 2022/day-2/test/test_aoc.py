import unittest
from src.aoc import get_score_for_old_rules
from src.aoc import get_score

class TestAoc(unittest.TestCase):

    def test_get_score_for_a_single_game_old_rules(self):        
        stringInput = 'A Z'
        result = get_score_for_old_rules(stringInput)
        self.assertEqual(result, 3)

    def test_get_score_for_multiple_games_old_rules(self):        
        stringInput = 'C X\nA Y\nB Z\nA X\nC Y'
        result = get_score_for_old_rules(stringInput)
        self.assertEqual(result, 30)

    def test_get_score_for_a_single_game_you_need_to_lose_for_a_rock(self):        
        stringInput = 'A X'
        result = get_score(stringInput)
        self.assertEqual(result, 3)    
    
    def test_get_score_for_a_single_game_you_need_to_lose_for_a_paper(self):        
        stringInput = 'B X'
        result = get_score(stringInput)
        self.assertEqual(result, 1)    

    def test_get_score_for_a_single_game_you_need_to_lose_for_a_scissors(self):        
        stringInput = 'C X'
        result = get_score(stringInput)
        self.assertEqual(result, 2)    

    def test_get_score_for_a_single_game_you_need_to_win_from_a_rock(self):        
        stringInput = 'A Z'
        result = get_score(stringInput)
        self.assertEqual(result, 8)    
    
    def test_get_score_for_a_single_game_you_need_to_win_from_a_paper(self):        
        stringInput = 'B Z'
        result = get_score(stringInput)
        self.assertEqual(result, 9)    

    def test_get_score_for_a_single_game_you_need_to_win_from_a_scissors(self):        
        stringInput = 'C Z'
        result = get_score(stringInput)
        self.assertEqual(result, 7)    

    def test_get_score_for_a_single_game_you_need_to_tie(self):        
        rockGameResult = get_score('A Y')
        paperGameResult = get_score('B Y')
        scissorsGameResult = get_score('C Y')
        
        self.assertEqual(rockGameResult, 4)    
        self.assertEqual(paperGameResult, 5)    
        self.assertEqual(scissorsGameResult, 6)    