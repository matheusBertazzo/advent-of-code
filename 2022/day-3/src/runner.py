import aoc
from pathlib import Path

path = str(Path(__file__).parent) + '/input/input.txt'

inputFile = open(path)
fileContent = inputFile.read()

result = aoc.get_priority(fileContent)
badgeResult = aoc.get_badge_priority(fileContent)

print(f'Result: {result}')
print(f'Badge result: {badgeResult}')
