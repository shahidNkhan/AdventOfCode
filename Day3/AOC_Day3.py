FILEPATH = './Day3/input_Day3.txt'


def getIncorrectItem(itemStr):
    # return the character that is present in both the first and second halves of the string
    itemSet = set()
    itemLength = len(itemStr)
    for index, item in enumerate(itemStr):
        if index < itemLength / 2:
            itemSet.add(item)
        elif item in itemSet:
            return item

def getCommonItem(itemStr1, itemStr2, itemStr3):
    # return the common character in the 3 strings
    itemSet1 = set(itemStr1)
    itemSet2 = set(itemStr2)
    itemSet3 = set(itemStr3)
    return (itemSet1 & itemSet2 & itemSet3).pop()


def getPriorityOfItem(item):
    # Lowercase item types a through z have priorities 1 through 26.
    # Uppercase item types A through Z have priorities 27 through 52.
    itemValue = ord(item)
    if itemValue <= 90:
        return itemValue - 65 + 27
    else:
        return itemValue - 97 + 1


def part1(inputFilePath):
    file = open(inputFilePath, 'r')
    incorrectItemSum = 0
    for row in file:
        misplacedItem = getIncorrectItem(row.strip('\n'))
        incorrectItemSum += getPriorityOfItem(misplacedItem)
    return incorrectItemSum

def part2(inputFilePath):
    file = open(inputFilePath, 'r')
    group = []
    badgeItemSum = 0
    for index, row in enumerate(file):
        group.append(row.strip('\n'))
        if (index+1) % 3 == 0:
            badgeItem = getCommonItem(group[0], group[1], group[2])
            group.clear()
            badgeItemSum += getPriorityOfItem(badgeItem)
    return badgeItemSum

if __name__ == '__main__':
    result1 = part1(FILEPATH)
    result2 = part2(FILEPATH)
    print(result1)
    print(result2)
