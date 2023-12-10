import time
start_time = time.time()
import uf
import math

lines = uf.read_lines("../in/9.in")[:-1]
tests = uf.read_lines("../test/9.in")[:-1]

def parse(lines):
    parsed = []
    for line in lines:
        numbers = line.split()
        
        parsed.append(list(map(int,numbers)))
    return parsed

def solve_row(row):
    nextrow = []
    first = []
    last = 0
    while not row.count(0) == len(row):
        for i in range(len(row) - 1):
            nextrow.append(row[i+1] - row[i])
        last += row[-1]
        first.append(row[0])
        row = nextrow
        nextrow = []
    res = 0
    while first:
        res = first.pop() - res
    return res,last

def solve(lines):
     firsts, lasts = zip(*map(solve_row,parse(lines)))
     return sum(lasts), sum(firsts)
 
print(solve(lines))


    

