import time
start_time = time.time()
import uf

lines = uf.read_lines("../in/14.in")[:-1]
tests = uf.read_lines("../test/14.in")[:-1]

def parse(input):
    res = []
    for line in input:
        res.append([c for c in line])
    return res

def fix_row(row):
    R = len(row) - 1
    for i in range(R, -1,-1):
        if row[i] == "O":
            j = i
            while (j < R and row[j+1] == "."):
                row[j] = "."
                row[j+1] = "O"
                j += 1
    return row

def rotate(matrix):
    t = list(map(list, zip(*matrix)))
    return [row[::-1] for row in t]

def count(m):
    r = rotate(m)
    total = 0
    for row in r:
        for i,c in enumerate(row):
            if c == "O":
                total += i+1
    return total

def p1(input):
    m = parse(input)
    r = rotate(m)
    r = [fix_row(row) for row in r]
    for _ in range(3):
        r = rotate(r)
    return count(r)

def cycle(matrix):
    r = matrix
    for _ in range(4):
        r = rotate(r)
        r = [fix_row(row) for row in r]
    return r

def p2(input):
    m = parse(input)
    seen = {}
    seen.setdefault(0)
    loop, c = 0, 0
    values = []
    while True:
        key = "".join([".".join(row) for row in m])
        if key not in seen.keys():
            seen[key] = 0
        if seen[key] != 0 and loop == 0:
            loop = c 
            break
        values.append(count(m))
        m = cycle(m)
        seen[key] = c
        c += 1
    start = seen[key]
    return values[start + ((1000000000-start) % (loop-start))]
    
print(p1(lines))
print(p2(lines))

print("--- %s seconds ---" % (time.time() - start_time))


