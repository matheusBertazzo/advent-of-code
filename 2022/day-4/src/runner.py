import aoc
from pathlib import Path

path = str(Path(__file__).parent) + '/input/input.txt'

inputFile = open(path)
fileContent = inputFile.read()

result = aoc.get_fully_contained_count(fileContent)
partiallyContainedResult = aoc.get_partially_contained_count(fileContent)

print(f'Result: {result}')
print(f'Partially contained result: {partiallyContainedResult}')
