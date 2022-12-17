FILEPATH = './input_Day6.txt'

def cIndex(item):
    # Lowercase item types a through z have priorities 1 through 26.
    # Uppercase item types A through Z have priorities 27 through 52.
    itemValue = ord(item)
    if itemValue <= 90:
        return itemValue - 65 + 27
    else:
        return itemValue - 97 + 1

def part1(inputFilePath):
    file = open(inputFilePath, 'r')
    for row in file:
        s = row.strip('\n')
        for i in range(len(s)-4):
            if len(set(s[i:i + 4])) == 4:
                return i+4


def part2(inputFilePath):
    file = open(inputFilePath, 'r')
    for row in file:
        s = row.strip('\n')
        for i in range(len(s)-14):
            if len(set(s[i:i + 14])) == 14:
                return i+14

if __name__ == '__main__':

    result1 = part1(FILEPATH)
    print(result1)

    result2 = part2(FILEPATH)
    print(result2)
