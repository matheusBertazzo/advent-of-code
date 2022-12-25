import unittest
from src.stack_parser import SuppliesInput, parse

class TestAoc(unittest.TestCase):

    def test_parse_given_a_single_item_in_each_stack(self):
        input: str = ''
        input += '[A] [B] [C]\n' 
        input += ' 1   2   3 \n'
        input += '\n'  

        result: SuppliesInput = parse(input)

        self.assertEqual(result.stacks[0], ['A'])
        self.assertEqual(result.stacks[1], ['B'])
        self.assertEqual(result.stacks[2], ['C'])

    def test_parse_given_two_items_in_each_stack(self):
        input: str = ''
        input += '[D] [E] [F]\n'
        input += '[G] [H] [I]\n' 
        input += ' 1   2   3 \n'
        input += '\n'  

        result = parse(input)
        
        self.assertEqual(result.stacks[0], ['G', 'D'])
        self.assertEqual(result.stacks[1], ['H', 'E'])
        self.assertEqual(result.stacks[2], ['I', 'F'])

    def test_parse_given_stacks_with_different_lengths(self):
        input: str = ''
        input += '        [F]\n'
        input += '[G] [H] [I]\n' 
        input += ' 1   2   3 \n'
        input += '\n'  

        result = parse(input)
        
        self.assertEqual(result.stacks[0], ['G'])
        self.assertEqual(result.stacks[1], ['H'])
        self.assertEqual(result.stacks[2], ['I', 'F'])

    def test_parse_given_stacks_and_the_command_list(self):
        input: str = ''
        input += '[G] [H] [I]\n' 
        input += ' 1   2   3 \n'
        input += '\n'  
        input += 'command 1\n'
        input += 'command 2\n'  

        result = parse(input)
        
        self.assertEqual(len(result.commands), 2)
        self.assertEqual(result.commands[0], 'command 1')
        self.assertEqual(result.commands[1], 'command 2')