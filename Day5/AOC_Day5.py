FILEPATH = './input_Day5.txt'
CRATES = [['H', 'C', 'R'],
          ['B', 'J', 'H', 'L', 'S', 'F'],
          ['R', 'M', 'D', 'H', 'J', 'T', 'Q'],
          ['S', 'G', 'R', 'H', 'Z', 'B', 'J'],
          ['R', 'P', 'F', 'Z', 'T', 'D', 'C', 'B'],
          ['T', 'H', 'C', 'G'],
          ['S', 'N', 'V', 'Z', 'B', 'P', 'W', 'L'],
          ['R', 'J', 'Q', 'G', 'C'],
          ['L', 'D', 'T', 'R', 'H', 'P', 'F', 'S']]

# CRATES = [['Z', 'N'],
#           ['M', 'C', 'D'],
#           ['P']]

def makeMove(source, sink, qt):
    if qt == 0:
        return
    crate = CRATES[source].pop()
    CRATES[sink].append(crate)
    makeMove(source, sink, qt-1)

def moveMultipleQuantity(source, sink, qt):
    if qt == 0:
        return
    craneInv = [CRATES[source].pop() for i in range(qt)]
    CRATES[sink].extend([craneInv.pop() for i in range(qt)])

def part1(inputFilePath):
    file = open(inputFilePath, 'r')
    result = ''
    for index, row in enumerate(file):
        if index >= 10:
            query = row.strip('\n').split(' ')
            qt = int(query[1])
            source = int(query[3]) - 1
            sink = int(query[5]) - 1
            makeMove(source, sink, qt)
    for row in CRATES:
        result += row.pop()
    return result

def part2(inputFilePath):
    file = open(inputFilePath, 'r')
    result = ''
    for index, row in enumerate(file):
        if index >= 10:
            query = row.strip('\n').split(' ')
            qt = int(query[1])
            source = int(query[3]) - 1
            sink = int(query[5]) - 1
            moveMultipleQuantity(source, sink, qt)
    for row in CRATES:
        result += row.pop()
    return result

if __name__ == '__main__':
    # result1 = part1(FILEPATH)
    # print(result1)

    result2 = part2(FILEPATH)
    print(result2)
