ROCK = 'A'
PAPER = 'B'
SCISSORS = 'C'

LOSS_SCORE = 0
ROCK_MODIFIER = 1
PAPER_MODIFIER = 2
SCISSORS_MODIFIER = 3

VICTORY_SCORE = 6
DRAW_SCORE = 3

scoreModifierDictionary: dict = dict()
scoreModifierDictionary[ROCK] = ROCK_MODIFIER
scoreModifierDictionary[PAPER] = PAPER_MODIFIER
scoreModifierDictionary[SCISSORS] = SCISSORS_MODIFIER

def calculate(opponentMove: str, yourMove: str) -> int:        
    if yourMove == ROCK:
        return __calculate_rps_score(opponentMove, yourMove, PAPER)        
    elif yourMove == PAPER:
        return __calculate_rps_score(opponentMove, yourMove, SCISSORS)
    else:
        return __calculate_rps_score(opponentMove, yourMove, ROCK)                

def __calculate_rps_score(opponentMove: str, yourMove: str, defeatMove: str):
    scoreModifier: int = scoreModifierDictionary[yourMove]
    
    if opponentMove == defeatMove:
        return LOSS_SCORE + scoreModifier
    elif opponentMove == yourMove:
        return  DRAW_SCORE + scoreModifier
    
    return VICTORY_SCORE + scoreModifier

