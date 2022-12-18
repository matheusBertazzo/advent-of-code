import string

def get_priority(input: str) -> int:
    rucksacks = input.split('\n')
    prioritySum = 0    
    
    for rucksack in rucksacks:
        lastIndex = len(rucksack)
        halfStringIndex = int(lastIndex/2)
        firstCompartment = rucksack[0:halfStringIndex]
        secondCompartment = rucksack[halfStringIndex:lastIndex]
        
        firstCompartmentDictionary: dict = __create_rucksack_dictionary(firstCompartment)
        prioritySum += __get_common_item_type_priority(secondCompartment, firstCompartmentDictionary)        

    return prioritySum

def __get_common_item_type_priority(rucksack: str, firstCompartmentDictionary: dict) -> int:
    for itemType in rucksack:
        if itemType in firstCompartmentDictionary:
            return string.ascii_letters.index(itemType) + 1             
    
    return 0

def get_badge_priority(input: str, groupSize: int = 3) -> int:
    rucksacks = input.split('\n')
    prioritySum = 0        
    isNewGroup: bool = True
    itemTypesDictionary: dict = dict()    

    for rucksackIndex in range(0, len(rucksacks)):
        rucksack = rucksacks[rucksackIndex]        
        
        if isNewGroup:
            itemTypesDictionary = __create_rucksack_dictionary(rucksack) 
            isNewGroup = False                       
            continue

        itemTypesDictionary = __filter_common_elements(itemTypesDictionary, rucksack)                        

        if(rucksackIndex + 1) % groupSize == 0:
            badge = list(itemTypesDictionary.keys())[0]
            prioritySum += string.ascii_letters.index(badge) + 1
            isNewGroup = True        
            
    return prioritySum

def __filter_common_elements(itemTypesDictionary: dict, rucksack: str) -> dict:
    auxItemTypesDictionary: dict = __create_rucksack_dictionary(rucksack)

    for itemType in list(itemTypesDictionary.keys()):
        if(itemType not in auxItemTypesDictionary):
            del itemTypesDictionary[itemType] 

    return itemTypesDictionary

def __create_rucksack_dictionary(rucksack: str) -> dict:
    itemTypesDictionary = dict()

    for itemType in rucksack:
        itemTypesDictionary[itemType] = True

    return itemTypesDictionary