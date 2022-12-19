class Interval:
    minValue: int
    maxValue: int    


def get_fully_contained_count(input: str) -> int: 
    intervalStrings = input.split('\n')
    fullyContainedCount: int = 0

    for intervalString in intervalStrings:
        firstInterval: Interval = __get_interval(intervalString, 0)
        secondInterval: Interval = __get_interval(intervalString, 1)

        if __isBigger(firstInterval, secondInterval):            
            if __is_fully_contained(secondInterval, firstInterval):
                fullyContainedCount += 1
                continue
        
        if __is_fully_contained(firstInterval, secondInterval):
            fullyContainedCount += 1

    return fullyContainedCount

def get_partially_contained_count(input: str) -> int:
    intervalStrings = input.split('\n')
    partiallyContainedCount: int = 0

    for intervalString in intervalStrings:
        firstInterval: Interval = __get_interval(intervalString, 0)
        secondInterval: Interval = __get_interval(intervalString, 1)

        if __is_partially_contained(firstInterval, secondInterval):
            partiallyContainedCount += 1         

    return partiallyContainedCount

def __is_partially_contained(firstInterval: Interval, secondInterval: Interval) -> bool:
    if firstInterval.minValue > secondInterval.maxValue or firstInterval.maxValue < secondInterval.minValue:
        return False
    
    return True

def __is_fully_contained(interval: Interval, biggerInterval: Interval) -> bool:
    if biggerInterval.minValue > interval.minValue or biggerInterval.maxValue < interval.maxValue:
        return False
    
    return True

def __get_interval(input: str, stringPartIndex: int) -> Interval:
    inputParts = input.split(',')
    firstIntervalString = inputParts[stringPartIndex]
    
    return __getIntervalFromString(firstIntervalString)

def __getIntervalFromString(firstIntervalString) -> Interval:
    interval: Interval = Interval()

    interval.minValue = int(firstIntervalString.split('-')[0])
    interval.maxValue = int(firstIntervalString.split('-')[1])
    
    return interval

def __isBigger(firstInterval: Interval, secondInterval: Interval) -> bool:
    firstIntervalSize  = firstInterval.maxValue - firstInterval.minValue + 1
    secondIntervalSize  = secondInterval.maxValue - secondInterval.minValue + 1

    return firstIntervalSize > secondIntervalSize