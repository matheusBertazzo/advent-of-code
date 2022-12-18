import aoc
from pathlib import Path

path = str(Path(__file__).parent) + '/input/input.txt'

inputFile = open(path)
fileContent = inputFile.read()

oldRulesResult = aoc.get_score_for_old_rules(fileContent)
result = aoc.get_score(fileContent)

print(f'Old rules score: {oldRulesResult}')
print(f'Score: {result}')
