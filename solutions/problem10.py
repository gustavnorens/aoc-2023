import time
start_time = time.time()
import uf
import math

dick = {
    "|": ["north", "south"],
    "-": ["west", "east"],
    "L": ["north", "east"],
    "7": ["west", "south"],
    "J": ["north", "west"],
    "F": ["south", "east"],
    "S": ["south", "east", "west", "north"],
    ".": [],
}


lines = uf.read_lines("../in/10.in")[:-1]
tests = uf.read_lines("../test/10.in")[:-1]

vertices = set()

def count_changes(j, line, r): #Part 2
    t = 0
p    for i in range(0, j):
        if line[i] in "F7|S" and (r,i) in vertices:
            t += 1
    if t % 2 == 1:
        return 1
    return 0

def solve(matrix):
    R,C = len(matrix), len(matrix[0])
    s1, s2 = 0, 0
    for i, line in enumerate(matrix):
        for j, c in enumerate(line):
            if c == "S":
                s1,s2 = i,j
    c1, c2 = s1, s2
    while True:
        if c1+1 < R and "north" in dick[matrix[c1+1][c2]] and "south" in dick[matrix[c1][c2]] and (c1+1,c2) not in vertices:
            c1 += 1
        elif c1-1 >= 0 and "south" in dick[matrix[c1-1][c2]] and "north" in dick[matrix[c1][c2]] and (c1-1,c2) not in vertices:
            c1 -= 1
        elif c2+1 < C and "west" in dick[matrix[c1][c2+1]] and "east" in dick[matrix[c1][c2]] and (c1,c2+1) not in vertices:
            c2 += 1
        elif c2-1 >= 0 and "east" in dick[matrix[c1][c2-1]] and "west" in dick[matrix[c1][c2]] and (c1,c2-1) not in vertices:
            c2 -= 1
        vertices.add((c1,c2))
        if (c1 == s1 and c2 == s2):
            break

    total = 0 #For part 2
    for i, line in enumerate(matrix): 
        for j, c in enumerate(line):
            if not (i,j) in vertices:
                total += count_changes(j,line,i)
    return len(vertices) // 2, total
  
res, total = solve(lines)

print(res, total)
print("--- %s seconds ---" % (time.time() - start_time))
