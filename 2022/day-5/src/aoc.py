from stack_parser import SuppliesInput, parse as parse_input
import re

def arrange_stacks(input: str) -> str: 
    suppliesInput: SuppliesInput = parse_input(input)
    result: str = ''

    for command in suppliesInput.commands:
        pattern = re.compile(r'move (?P<amountOfPops>\d+) from (?P<target>\d+) to (?P<destination>\d+)')
        match = pattern.match(command)

        amountOfPops = int(match.group('amountOfPops'))
        targetStack = int(match.group('target')) - 1
        destinationStack = int(match.group('destination')) - 1

        for currentPop in range(0, amountOfPops):
            suppliesInput.stacks[destinationStack].append(suppliesInput.stacks[targetStack].pop())

    for stack in suppliesInput.stacks:
        result += stack.pop()


    return result    