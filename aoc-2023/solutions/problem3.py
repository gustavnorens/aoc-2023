import uf
import time
start_time = time.time()
input = uf.read_lines("input3.txt")[:-1]

testInput = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    ".....755..",
    "...$.*....",
    ".664.755..",
    ]


def p1(matrix):
    sum = 0
    for i, line in enumerate(matrix):
        for j, c in enumerate(line):
            isNum, length = isNumber(j,line)
            if isNum:
                if isAdjacent(matrix, i, j, length):
                    sum += parse(j,line, length)
    return sum

def isNumber(j, line):
    for i in range(3, 0, -1):
        if line[j:j+i].isdigit() and ((not line[j-1].isdigit()) or j-1 == -1 ):
            return True, i
    return False, -1

def isAdjacent(matrix, k, m, length):
    R = len(matrix)
    C = len(matrix[0])
    for i in range(k-1,k+2):
        for j in range(m-1,m+length+1):
            if 0 <= i < R  and 0 <= j < C:
                if matrix[i][j] in "+*#=/$&@%-":
                    return True
    return False

def parse(i, line, length):
    return int(line[i:i+length])


def p2(matrix):
    sum = 0
    for i, line in enumerate(matrix):
        for j, elem in enumerate(matrix):
            if matrix[i][j] == "*":
               sum += gearParser(matrix, i, j)
    return sum

def gearParser(matrix, k, m):
    indices = []
    for i in range(k-1, k+2):
        for j in range(m-1, m+2):
            if matrix[i][j].isdigit():
                indices.append((i,j))
    numbers = getNumbers(indices, matrix)
    if len(numbers) == 2:
        return numbers[0][0] * numbers[1][0]
    else:
        return 0

def getNumbers(indices, matrix):
    numbers = []
    for i,j in indices:
        numbers.append(getNumber(j, matrix[i], i))
    return list(set(numbers))

def getNumber(i, line, lineNumber):
    number = ""
    while(line[i-1].isdigit()):
        i -= 1
    start = i
    while i < len(line) and line[i].isdigit():
        number += line[i]
        i += 1
    return int(number), start, lineNumber

print(p1(input))
print(p2(input))

print("--- %s seconds ---" % (time.time() - start_time))
