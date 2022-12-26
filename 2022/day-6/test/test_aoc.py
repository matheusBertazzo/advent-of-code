import unittest
from src.aoc import get_first_marker_index

class TestAoc(unittest.TestCase):

    def test_get_first_marker_index_for_default_example_1(self):            
        result = get_first_marker_index('mjqjpqmgbljsphdztnvjfqwrcgsmlb')
        self.assertEqual(result, 7)

    def test_get_first_marker_index_for_default_example_2(self):            
        result = get_first_marker_index('bvwbjplbgvbhsrlpgdmjqwftvncz')
        self.assertEqual(result, 5)
    
    def test_get_first_marker_index_for_default_example_3(self):            
        result = get_first_marker_index('nppdvjthqldpwncqszvftbrmjlhg')
        self.assertEqual(result, 6)
    
    def test_get_first_marker_index_for_default_example_4(self):            
        result = get_first_marker_index('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg')
        self.assertEqual(result, 10)
    
    def test_get_first_marker_index_for_default_example_5(self):            
        result = get_first_marker_index('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw')
        self.assertEqual(result, 11)

    def test_get_first_marker_index_for_default_example_6(self):            
        result = get_first_marker_index('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 14)
        self.assertEqual(result, 19)

    def test_get_first_marker_index_for_default_example_7(self):            
        result = get_first_marker_index('bvwbjplbgvbhsrlpgdmjqwftvncz', 14)
        self.assertEqual(result, 23)
    
    def test_get_first_marker_index_for_default_example_8(self):            
        result = get_first_marker_index('nppdvjthqldpwncqszvftbrmjlhg', 14)
        self.assertEqual(result, 23)
    
    def test_get_first_marker_index_for_default_example_9(self):            
        result = get_first_marker_index('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 14)
        self.assertEqual(result, 29)
    
    def test_get_first_marker_index_for_default_example_10(self):            
        result = get_first_marker_index('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 14)
        self.assertEqual(result, 26)