FILEPATH = './input_Day7.txt'

class Node:
   def __init__(self, fname=None):
      self.f_name = fname
      self.next_fs = []
      self.prev_f = None
      self.size = 0
      self.isFile = False

class DLinkedList:
   def __init__(self):
      self.head = None

def getChildNode(node, fname):
    for f in node.next_fs:
        if f.isFile == False and f.f_name == fname:
            return f

def part1(inputFilePath):
    l1 = DLinkedList()
    l1.head = Node("/")
    curNode = l1.head
    file = open(inputFilePath, 'r')
    for index, row in enumerate(file):
        if index == 0: continue
        words = row.strip('\n').split(' ')
        if words[0] == '$':
            if words[1] == 'cd':
                if words[2] == '..':
                    curNode = curNode.prev_f
                else:
                    curNode = getChildNode(curNode, words[2])
        else:
            dNext = Node(words[1])
            dNext.prev_f = curNode
            curNode.next_fs.append(dNext)

            if words[0] != 'dir':
                dNext.size = int(words[0])
                dNext.isFile = True
                curNode.size += int(words[0])
    validDirs = []
    recIterate(validDirs, l1.head)
    validSum = 0
    for directory in validDirs:
        validSum += directory.size
    return l1.head, validSum

def recIterate(validDirs, node):
    node.size = 0
    for n in node.next_fs:
        if n.isFile == True:
            node.size += n.size
        else:
            node.size += recIterate(validDirs, n)
    if node.size <= 100000:
        validDirs.append(node)

    return node.size

def part2(node):
    reqSize = 30000000 - (70000000 - node.size)
    bestNode = node
    stack = []
    stack.append(node)
    while len(stack) > 0:
        n = stack.pop()
        if n.size > reqSize and n.size < bestNode.size:
            bestNode = n
        for nc in n.next_fs:
            if nc.isFile == False:
                stack.append(nc)
    return bestNode.size

if __name__ == '__main__':

    node, result1 = part1(FILEPATH)
    print(result1)

    result2 = part2(node)
    print(result2)
