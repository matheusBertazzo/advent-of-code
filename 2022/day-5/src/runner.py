import aoc
from pathlib import Path

path = str(Path(__file__).parent) + '/input/input.txt'

inputFile = open(path)
fileContent = inputFile.read()

result = aoc.arrange_stacks_with_create_arrenger_9000(fileContent)
result9001 = aoc.arrange_stacks_with_create_arrenger_9001(fileContent)

print(f'Result: {result}')
print(f'Result 9001: {result9001}')