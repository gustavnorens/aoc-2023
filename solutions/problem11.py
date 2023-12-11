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
    total = 0
    while stack:
        print(stack)
        current = stack.pop()
        total += distance(stack, current, empties)
    return total
        

def distance(stack, start, empties):
    i,j = start
    total = 0
    rows = empties[0]
    cols = empties[1]
    for x,y in stack:
        i, j = start
        i, x = min(i,x), max(i,x)
        j, y = min(j,y), max(j,y)
        for row in rows:
            if i <= row <= x:
                total += 999999
        for col in cols:
            if j <= col <= y:
                total += 999999
        total += abs(x-i) + abs(y-j)
        
    return total
    
print(solve(lines))











                
                
