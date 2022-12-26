def get_first_marker_index(input: str, requiredDistinctStreak: int = 4) -> int: 
    
    currentCharIndex = 0
    markDictionary: dict = dict()

    while currentCharIndex < len(input):
        currentChar = input[currentCharIndex]

        if currentChar in markDictionary:
            if len(markDictionary) < requiredDistinctStreak:
                currentCharIndex = markDictionary[currentChar] + 1
                markDictionary.clear()
                currentChar = input[currentCharIndex]
                markDictionary[currentChar] = currentCharIndex

        if not len(markDictionary) < requiredDistinctStreak:
            return currentCharIndex

        markDictionary[currentChar] = currentCharIndex
        currentCharIndex += 1

    return 0