import time
start_time = time.time()
import uf

lines = uf.read_lines("../in/21.in")[:-1]
tests = uf.read_lines("../test/21-2.in")[:-1]

def parse(puzzle):
    m = [[c for c in line] for line in puzzle]
    return m

m = parse(lines)

even_steps = 7546
odd_steps = 7539
row_len = len(m)
col_len = len(m[0])

s = -1, -1
for i, row in enumerate(m):
    for j, c in enumerate(row):
        if c == "S":
            s = i, j

def neighbours(cells):
    seen = set()
    for x,y in cells:
        for nx, ny in [(0,1), (1,0), (-1,0), (0,-1)]:
            if m[(x+nx) % len(m)][(y+ny) % len(m[0])] != "#":
                seen.add((x+nx,y+ny))
    return list(seen)

def _neighbours(cells):
    seen = set()
    for x,y in cells:
        for nx, ny in [(0,1), (1,0), (-1,0), (0,-1)]:
            i = x+nx
            j = y+ny
            if i >= 0 and i < len(m) and j >= 0 and j < len(m[0]) and m[i][j] != "#":
                seen.add((i,j))
    return list(seen)
     