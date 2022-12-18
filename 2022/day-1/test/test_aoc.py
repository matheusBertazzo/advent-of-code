import unittest
from src.aoc import get_max_calories

class TestAoc(unittest.TestCase):

    def test_get_the_max_amount_of_calories_in_list_given_a_single_elf(self):        
        stringInput = '1'
        result = get_max_calories(stringInput)
        self.assertEqual(result, 1)

    def test_get_the_max_amount_of_calories_in_list(self):                
        result = get_max_calories('1\n\n2\n\n3\n\n')
        self.assertEqual(result, 3)

    def test_get_the_max_amount_of_calories_in_list_given_more_than_one_package_per_elf(self):                    
        result = get_max_calories('1\n\n2\n2\n2\n\n3\n\n')
        self.assertEqual(result, 6)

    def test_get_the_max_amount_of_calories_for_top_3_elves_in_list_given_more_than_3_elves_per_elf(self):                    
        result = get_max_calories('1\n\n2\n\n3\n\n4\n\n', 3)
        self.assertEqual(result, 9)