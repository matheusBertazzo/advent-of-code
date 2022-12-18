from src.rps_calculator import calculate

normalizedMoveDictionary: dict = dict()
normalizedMoveDictionary['X'] = 'A'
normalizedMoveDictionary['Y'] = 'B'
normalizedMoveDictionary['Z'] = 'C'

loseDictionary: dict = dict()
loseDictionary['A'] = 'C'
loseDictionary['B'] = 'A'
loseDictionary['C'] = 'B'

winDictionary: dict = dict()
winDictionary['A'] = 'B'
winDictionary['B'] = 'C'
winDictionary['C'] = 'A'

def get_score_for_old_rules(input: str) -> int:
    games = input.split('\n')
    finalScore = 0

    for game in games:
        opponentMove = __get_opponent_move(game)
        yourMove = __get_your_move_for_old_rules(game)
        finalScore += calculate(opponentMove, yourMove)

    return finalScore

def get_score(input: str) -> int:
    games = input.split('\n')
    finalScore = 0

    for game in games:
        opponentMove = __get_opponent_move(game)
        yourMove = __get_your_move(game, opponentMove)
        finalScore += calculate(opponentMove, yourMove)

    return finalScore

def __get_opponent_move(game: str) -> str:
    return game.split(' ')[0]

def __get_your_move_for_old_rules(game: str) -> str:
    return normalizedMoveDictionary[game.split(' ')[1]]

def __get_your_move(game: str, opponentMove: str) -> str:
    yourMove = game.split(' ')[1]
    
    if yourMove == 'X':
        return loseDictionary[opponentMove]
    elif yourMove == 'Z':
        return winDictionary[opponentMove]

    return opponentMove
