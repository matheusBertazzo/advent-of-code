import unittest
from src.aoc import get_priority
from src.aoc import get_badge_priority

class TestAoc(unittest.TestCase):

    def test_get_priority_for_single_rucksack_given_a_lower_case_item_type(self):            
        result = get_priority('apbcpd')
        self.assertEqual(result, 16) 
    
    def test_get_priority_for_single_rucksack_given_an_upper_case_item_type(self):            
        result = get_priority('aLbcLd')
        self.assertEqual(result, 38) 
    
    def test_get_priority_for_multiple_rucksacks(self):            
        result = get_priority('aLbcLd\napbcpd')
        self.assertEqual(result, 54) 

    def test_get_priority_for_multiple_rucksacks_with_repeated_item_types(self):            
        result = get_priority('vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\nPmmdzqPrVvPwwTWBwg\nwMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\nttgJtRGJQctTZtZT\nCrZsJsPPZsGzwwsLwLmpwMDw')
        self.assertEqual(result, 157) 

    def test_get_badge_priority_for_multiple_rucksacks(self):            
        result = get_badge_priority('vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\nPmmdzqPrVvPwwTWBwg\nwMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\nttgJtRGJQctTZtZT\nCrZsJsPPZsGzwwsLwLmpwMDw')
        self.assertEqual(result, 70) 