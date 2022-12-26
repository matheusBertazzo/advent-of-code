import unittest
from src.aoc import arrange_stacks_with_create_arrenger_9000, arrange_stacks_with_create_arrenger_9001

class TestAoc(unittest.TestCase):

    def test_arrange_stacks_for_an_input_that_moves_one_object_at_a_time(self):            
        input: str = ''
        input += '[A] [B] [C]\n'
        input += '[A] [B] [C]\n' 
        input += ' 1   2   3 \n'
        input += '\n'
        input += 'move 1 from 1 to 3\n'
        input += 'move 1 from 2 to 1\n'  

        result = arrange_stacks_with_create_arrenger_9000(input)

        self.assertEquals('BBA', result)


    def test_arrange_stacks_for_an_input_that_moves_more_than_one_object_at_a_time(self):            
        input: str = ''
        input += '[A] [B] [C]\n'
        input += '[A] [B] [C]\n' 
        input += ' 1   2   3 \n'
        input += '\n'
        input += 'move 2 from 1 to 3\n'
        input += 'move 1 from 3 to 1\n'  

        result = arrange_stacks_with_create_arrenger_9000(input)

        self.assertEquals('ABA', result)

    def test_arrange_stacks_for_an_input_that_moves_one_object_at_a_time(self):            
        input: str = ''
        input += '[A] [B] [C]\n'
        input += '[D] [E] [F]\n' 
        input += ' 1   2   3 \n'
        input += '\n'
        input += 'move 1 from 1 to 3\n'
        input += 'move 1 from 1 to 3\n'
        input += 'move 2 from 3 to 1\n'  

        result = arrange_stacks_with_create_arrenger_9001(input)

        self.assertEquals('DBC', result)


    def test_arrange_stacks_for_an_input_that_moves_more_than_one_object_at_a_time(self):            
        input: str = ''
        input += '[A] [B] [C]\n'
        input += '[D] [E] [F]\n' 
        input += ' 1   2   3 \n'
        input += '\n'
        input += 'move 2 from 1 to 3\n'
        input += 'move 2 from 3 to 1\n'  

        result = arrange_stacks_with_create_arrenger_9001(input)

        self.assertEquals('ABC', result)