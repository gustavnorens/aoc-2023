import time
start_time = time.time()
import uf
import math

lines = uf.read_lines("../in/11.in")[:-1]
tests = uf.read_lines("../test/11.in")[:-1]


def parse(lines):
    matrix = []
    empty = [[],[]]
    for i, line in enumerate(lines):
        if "#" not in line:
            empty[0].append(i)
        matrix.append([char for char in line])

    transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))] 
    new = []
    for i,row in enumerate(transposed):
        if "#" not in row:
           empty[1].append(i)
           
    matrix = [[row[i] for row in transposed] for i in range(len(transposed[0]))]

    return matrix, empty


def solve(lines):
    matrix, empties = parse(lines)
    stack = []
    for i, row in enumerate(matrix):
        for j, elem in enumerate(row):
            if elem == "#":
                stack.append((i,j))
    p1, p2 = 0, 0
    while stack:
        current = stack.pop()
        p1 += distance(stack, current, empties, 2)
        p2 += distance(stack, current, empties, 1000000)
    return p1, p2
        

def distance(stack, start, empties, n):
    total = 0
    i, j = start
    for x,y in stack:
        x1, x2 = min(i,x), max(i,x)
        y1, y2 = min(j,y), max(j,y)
        for row in empties[0]:
            if x1 <= row <= x2:
                total += n-1
        for col in empties[1]:
            if y1 <= col <= y2:
                total += n-1
        total += abs(x2-x1) + abs(y2-y1)
    return total
    
print(solve(lines))
print("--- %s seconds ---" % (time.time() - start_time))










                
                
