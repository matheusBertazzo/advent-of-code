import aoc
from pathlib import Path

path = str(Path(__file__).parent) + '/input/input.txt'

inputFile = open(path)
fileContent = inputFile.read()

result = aoc.get_first_marker_index(fileContent)
result = aoc.get_first_marker_index(fileContent, 14)

print(f'Result: {result}')
print(f'Message result: {result}')
