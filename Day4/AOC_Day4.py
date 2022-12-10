FILEPATH = './input_Day4.txt'

def checkIfEncompassed(ranges):
    range1 = [eval(i) for i in ranges[0].split('-')]
    range2 = [eval(i) for i in ranges[1].split('-')]

    if range1[0] == range2[0]: return True
    if range1[1] == range2[1]: return True
    if range1[0] < range2[0] and range1[1] > range2[1]: return True
    if range1[0] > range2[0] and range1[1] < range2[1]: return True

    return False

def checkIfOverlap(ranges):
    if checkIfEncompassed(ranges): return True

    range1 = [eval(i) for i in ranges[0].split('-')]
    range2 = [eval(i) for i in ranges[1].split('-')]

    if range1[0] >= range2[0] and range1[0] <= range2[1]: return True
    if range1[1] >= range2[0] and range1[1] <= range2[1]: return True

    return False

def part1(inputFilePath):
    file = open(inputFilePath, 'r')
    numberOfEncompassed = 0
    for row in file:
        if checkIfEncompassed(row.strip('\n').split(',')):
            numberOfEncompassed += 1
    return numberOfEncompassed

def part2(inputFilePath):
    file = open(inputFilePath, 'r')
    numberOfOverlaps = 0
    for row in file:
        if checkIfOverlap(row.strip('\n').split(',')):
            numberOfOverlaps += 1
    return numberOfOverlaps

if __name__ == '__main__':
    result1 = part1(FILEPATH)
    print(result1)

    result2 = part2(FILEPATH)
    print(result2)
