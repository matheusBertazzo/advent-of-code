def get_max_calories(input: str, topElvesToSum:int = 1) -> int:
    input.split('\n')
    lines: list = input.split('\n')
    currentIndex: int = 0   
    currentElf: int = 0     
    currentCalories: int = 0
    calories = list()
    calories.append(0)

    while currentIndex < len(lines):        
        currentCalories = lines[currentIndex]        
        currentIndex += 1
        
        if currentCalories == '':            
            currentElf += 1
            calories.append(0)
            continue
        
        calories[currentElf] = calories[currentElf] + int(currentCalories)              
    

    calories.sort(reverse = True)
    calories = calories[0:topElvesToSum]

    return sum(calories)
