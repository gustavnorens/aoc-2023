import time
start_time = time.time()
import uf

lines = uf.read_lines("../in/22.in")[:-1]
tests = uf.read_lines("../test/22.in")[:-1]

def segment(a,b,c): 
    ax, ay, _ = a
    bx, by, _ = b
    cx, cy, _ = c

    if ( (bx <= max(ax, cx)) and (bx >= min(ax, cx)) and 
           (by <= max(ay, cy)) and (by >= min(ay, cy))): 
        return True
    return False
  
def orientation(a,b,c): 
    ax, ay, _ = a
    bx, by, _ = b
    cx, cy, _ = c
    val = (by - ay) * (cx - bx) - (bx - ax) * (cy - by)
    if (val > 0): 
        return 1
    elif (val < 0): 
        return 2
    else: 
        return 0
  
def intersection(a,b,c,d): #GeeksForGeeks, shite code
    o1 = orientation(a, b, c) 
    o2 = orientation(a, b, d) 
    o3 = orientation(c, d, a) 
    o4 = orientation(c, d, b) 
  
    if o1 != o2 and o3 != o4: 
        return True
    if o1 == 0 and segment(a, c, b): 
        return True
    if o2 == 0 and segment(a, d, b): 
        return True
    if o3 == 0 and segment(c, a, d): 
        return True
    if o4 == 0 and segment(c, b, d): 
        return True
    return False

def parse(puzzle):
    bricks = []
    puzzle = sorted(puzzle, key=lambda x: int(x.split("~")[0].split(",")[2]))
    for line in puzzle:
        fst, snd = line.split("~")
        fx,fy,fz = map(int,fst.split(","))
        sx,sy,sz = map(int,snd.split(","))
        bricks.append(((fx,fy,fz), (sx,sy,sz)))
    return bricks

def build_tower(puzzle):
    bricks = parse(puzzle)
    tower = []
    for brick in bricks:
        diff = brick[1][2]-brick[0][2]
        highest = 1
        for ob in tower:
            if intersection(brick[0], brick[1], ob[0], ob[1]):
                z_level = ob[1][2]
                if z_level >= highest:
                    highest = z_level + 1
        tower.append(((brick[0][0],brick[0][1],highest), (brick[1][0],brick[1][1],diff+highest)))
    return tower 

def can_remove(brick, stack, i):
    bricks_above = []
    for j in range(i, len(stack)):
        ob = stack[j]
        if intersection(brick[0],brick[1],ob[0],ob[1]) and ob[0][2] - 1 == brick[1][2]:
            bricks_above.append((j, False))
    
    for k in range(j,-1,-1):
        b = stack[k]
        for p, (n, _) in enumerate(bricks_above):
            ob = stack[n]
            if b[1][2] == ob[0][2] - 1 and intersection(b[0],b[1],ob[0],ob[1]) and k != i:
                bricks_above[p] = n, True

    return all([ticked for _, ticked in bricks_above])

def count(puzzle):
    stack = build_tower(puzzle)
    total = 0
    for i, brick in enumerate(stack):
        if can_remove(brick, stack, i):
            total += 1
    return total

def p2(puzzle):
    stack = build_tower(puzzle)
    total = 0
    depends = {i: [] for i in range(len(stack))}
    supports = {i: [] for i in range(len(stack))}
    for i, brick in enumerate(stack):
        for j, ob in enumerate(stack):
            if intersection(brick[0],brick[1],ob[0],ob[1]) and brick[0][2] - 1 == ob[1][2]:
                depends[i].append(j)
                supports[j].append(i)

    print(depends)
    print(supports)
    for i, brick in enumerate(stack):
        s = [i]
        removed = []
        while s:
            v = s.pop()
            for num in supports[v]:
                if len([x for x in depends[num] if x not in removed]) == 1:
                    print(num)
                    total += 1
                    s.append(num)
            removed.append(v)
    return total

print(count(lines))
print(p2(lines))

print("--- %s seconds ---" % (time.time() - start_time))   