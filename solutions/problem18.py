import time
start_time = time.time()
import uf
import copy

lines = uf.read_lines("../in/18.in")[:-1]
tests = uf.read_lines("../test/18.in")[:-1]

def parse(puzzle):
    x1, y1 = 0, 0
    x2, y2 = 0, 0
    squares = []
    boundrary_p1 = 0
    boundrary_p2 = 0
    colors = []
    for dir,length,color in map(parse_line,puzzle):
        if dir == "R":
            y1 += length
        elif dir == "D":
            x1 += length
        elif dir == "U":
            x1 -= length
        elif dir == "L":
            y1 -= length

        boundrary_p1 += length
        squares.append((x1,y1))

        dir = color[-2]
        color = color[2:-2]

        length = int(color, 16)

        if dir == "0":
            y2 += length
        elif dir == "1":
            x2 += length
        elif dir == "3":
            x2 -= length
        elif dir == "2":
            y2 -= length

        boundrary_p2 += length
        colors.append((x2,y2))
    return squares, boundrary_p1, colors, boundrary_p2

def parse_line(line):
    dir, length, color = line.split()
    length = int(length)
    return dir, length, color
 
def flood(edge, start):
    stack = [start]
    seen = set()
    k = 0
    while stack:
        x, y = stack.pop()
        if (x,y) in seen or (x,y) in edge: 
            continue
        seen.add((x,y))
        for dx,dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            stack.append((x+dx, y+dy))
        k += 1
    return k

def ray(cords):
    cords, line = ray_parse(cords)
    cords = cords[1:-1]
    total = 0
    for row in cords:
        total += calc_row(row,line)
    return total

def calc_row(row, line):
    tot = 0
    ys = []
    curr = False
    inside = 0
    for x,y in row:
        if line[(x,y)]:
            curr = not curr
            ys.append((x,y))
        if curr:
            inside += 1
    for i in range(0,len(ys)-1,2):
        tot += abs(ys[i][1] - ys[i+1][1])
    return tot - inside

def ray_parse(cords):
    important = {}
    for x,y in cords:
        if (x-1,y) in cords:
            important[(x,y)] = True
        else:
            important[(x,y)] = False
    cords = list(sorted(cords))
    
    new_cords = []
    c = []
    current = cords[0][0]
    for x,y in cords:
        if current == x:
            c.append((x,y))
        else: 
            new_cords.append(copy.deepcopy(c))
            c = []
            c.append((x,y))
            current = x
    new_cords.append(c)
    return new_cords, important

def trapezoid(cords):
    total = 0
    for i in range(len(cords)):
        fx,fy = cords[i]
        sx,sy = cords[(i+1) % len(cords)]
        dx = fx - sx
        dy = fy + sy
        total += dx * dy
    return abs(total // 2)

def picks_theorem(cords, b):
    A = trapezoid(cords)
    i = A - (b // 2) + 1
    return i + b

def solve(puzzle):
    part1, b1, part2, b2 = parse(puzzle)
    return picks_theorem(part1,b1), picks_theorem(part2,b2)

print(solve(lines))

print("--- %s seconds ---" % (time.time() - start_time))