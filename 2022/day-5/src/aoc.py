from stack_parser import SuppliesInput, parse as parse_input
import re

def arrange_stacks_with_create_arrenger_9000(input: str) -> str: 
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

def arrange_stacks_with_create_arrenger_9001(input: str) -> str: 
    suppliesInput: SuppliesInput = parse_input(input)
    result: str = ''

    for command in suppliesInput.commands:
        pattern = re.compile(r'move (?P<amountOfPops>\d+) from (?P<target>\d+) to (?P<destination>\d+)')
        match = pattern.match(command)

        amountOfPops = int(match.group('amountOfPops'))
        targetStackIndex = int(match.group('target')) - 1
        destinationStackIndex = int(match.group('destination')) - 1

        destinationStack = suppliesInput.stacks[destinationStackIndex]
        targetStack = suppliesInput.stacks[targetStackIndex]

        destinationStack.extend(targetStack[-amountOfPops : len(targetStack)])
    
        for currentPop in range(0, amountOfPops):
            targetStack.pop()

    for stack in suppliesInput.stacks:
        result += stack.pop()


    return result    