import time
import copy
start_time = time.time()
import uf

lines = uf.read_lines("../in/13.in")[:-1]

def from_matrix(matrix, n, avoid):
    lines = []
    for i in range(len(matrix)-1):
        if matrix[i] == matrix[i+1]:
            if pattern(matrix,i,i+1) and (i+1) * n != avoid:
                return (i+1) * n
    return 0

def pattern(matrix, i, j):
    while (i >= 0 and j <= len(matrix) - 1):
        if matrix[i] != matrix[j]:
            return False
        i -= 1
        j += 1
    return True

def transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

def parse(input):
    matrices = []
    matrix = []
    for line in input:
        if line != "":
            matrix.append([c for c in line])
        else:
            matrices.append(matrix)
            matrix = []
    matrices.append(matrix)
    return matrices

def solve(input):
    matrices = parse(input)
    p1 = 0
    p2 = 0 
    for matrix in matrices:
        m,r = from_m(matrix)
        
        p1 += from_matrix(matrix, 100,-1)
        p1 += from_matrix(transpose(matrix), 1,-1)
        p2 += r
    return p1,p2

def flip(c):
    if c == "#":
        return "."
    elif c == ".":
        return "#"

def from_m(m):
    matrices = []
    p = from_matrix(m,100, -1)
    q = from_matrix(transpose(m),1,-1)
    res = p
    if p == 0:
        res = q
    for i, row in enumerate(m):
        for j, elem in enumerate(row):
            new = copy.deepcopy(m)
            new[i][j] = flip(elem)
            np = from_matrix(new,100,p)
            nq = from_matrix(transpose(new),1,q)
            if (p,q) != (np,nq) and (np > 0 or nq > 0):
                if np == res:
                    return new, nq
                elif nq == res:
                    return new, np
                elif np == 0:
                    return new, nq
                elif nq == 0:
                    return new, np
    
print(solve(lines))
