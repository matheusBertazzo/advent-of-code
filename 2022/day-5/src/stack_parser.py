import math

class SuppliesInput:
    stacks: list[list[str]]
    commands: list[str]

FIRST_ITEM_INDEX: int = 1

def parse(input: str) -> SuppliesInput:
    result = SuppliesInput()
    lines = input.split('\n')

    result.stacks = __parse_stacks(lines)
    result.commands = __parse_commands(lines)

    return result

def __parse_commands(lines: list[str]):
    isCommandLine = False
    commands = []
    for line in lines:

        if isCommandLine:
            if line != '' :
                commands.append(line)
            continue

        if line == '':
            isCommandLine = True

    return commands

def __parse_stacks(lines: list[str]) -> list[list[str]]:
    stacks = __allocate_stacks(lines)

    for line in lines:
        currentItemIndex = FIRST_ITEM_INDEX
        
        currentItem = line[currentItemIndex]

        if currentItem.isnumeric():
            break

        __parse_single_input_line(stacks, line)


    return __to_list_of_stacks(stacks)

def __to_list_of_stacks(listOfLists):
    for stack in listOfLists:
        stack.reverse()

    return listOfLists

def __parse_single_input_line(stacks, line):
    ITEM_INTERVAL = 4
    currentStackIndex = 0
    currentItemIndex = FIRST_ITEM_INDEX

    while currentItemIndex < len(line):
        currentItem = line[currentItemIndex]

        if currentItem != ' ':
            stacks[currentStackIndex].append(currentItem)

        currentStackIndex += 1
        currentItemIndex += ITEM_INTERVAL

def __allocate_stacks(lines) -> list[list[str]]:
    stacks: list[list[str]] = []
    numberOfStacksNeeded = math.ceil(len(lines[0]) / 4)
    
    for count in range(0, numberOfStacksNeeded): 
        stacks.append([])

    return stacks