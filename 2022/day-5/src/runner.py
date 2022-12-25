import aoc
from pathlib import Path

path = str(Path(__file__).parent) + '/input/input.txt'

inputFile = open(path)
fileContent = inputFile.read()

result = aoc.arrange_stacks(fileContent)

print(f'Result: {result}')