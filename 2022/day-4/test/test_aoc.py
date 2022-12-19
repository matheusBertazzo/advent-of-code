import unittest
from src.aoc import get_fully_contained_count
from src.aoc import get_partially_contained_count

class TestAoc(unittest.TestCase):

    def test_get_fully_contained_count_for_single_input_line_that_doesnt_overlap(self):            
        result = get_fully_contained_count('1-3, 4-6')
        self.assertEqual(result, 0)
    
    def test_get_fully_contained_count_for_single_input_line_given_first_interval_is_bigger(self):            
        result = get_fully_contained_count('3-6, 4-6')
        self.assertEqual(result, 1)   

    def test_get_fully_contained_count_for_single_input_line_given_second_interval_is_bigger(self):            
        result = get_fully_contained_count('4-6, 1-7')
        self.assertEqual(result, 1) 

    def test_get_fully_contained_count_for_single_input_line_given_first_and_second_interval_are_the_same(self):            
        result = get_fully_contained_count('5-8, 5-8')
        self.assertEqual(result, 1)

    def test_get_fully_contained_count_for_multiple_input_lines(self):            
        result = get_fully_contained_count('1-3, 4-6\n3-6, 4-6\n4-6, 1-7\n5-8, 5-8')
        self.assertEqual(result, 3)

    def test_get_partially_contained_count_for_single_input_line_that_doesnt_overlap(self):
        result = get_partially_contained_count('1-3, 4-6')
        self.assertEqual(result, 0)
    
    def test_get_partially_contained_count_for_single_input_line_that_partially_overlap_given_first_interval_is_bigger(self):
        result = get_partially_contained_count('1-4, 4-6')
        self.assertEqual(result, 1)

    def test_get_partially_contained_count_for_single_input_line_that_partially_overlap_given_second_interval_is_bigger(self):
        result = get_partially_contained_count('6-8, 1-6')
        self.assertEqual(result, 1)
    
    def test_get_partially_contained_count_for_single_input_line_given_first_and_second_interval_are_the_same(self):            
        result = get_partially_contained_count('5-8, 5-8')
        self.assertEqual(result, 1)

    def test_get_partially_contained_count_for_multiple_input_lines(self):            
        result = get_partially_contained_count('1-3, 4-6\n1-4, 4-6\n6-8, 1-6\n5-8, 5-8')
        self.assertEqual(result, 3)
