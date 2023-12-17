import time
start_time = time.time()
import uf

lines = uf.read_lines("../in/16.in")[:-1]
tests = uf.read_lines("../test/16.in")[:-1]

dict = {}

def parse(puzzle):
    return [[c for c in line] for line in puzzle]

def move(t, d):
    a,b = t
    if d == 0:
        return a,b+1
    elif d == 1:
        return a+1,b
    elif d == 2:
        return a,b-1
    elif d == 3:
        return a-1,b
    return None

def new_dir(s,d):
    if s == "/":
        if d == 0:
            return 3
        elif d == 1:
            return 2
        elif d == 2:
            return 1
        elif d == 3:
            return 0
    elif s == "\\":
        if d == 0:
            return 1
        elif d == 1:
            return 0
        elif d == 2:
            return 3
        elif d == 3:
            return 2
    return None


def traverse_path(m, start, dir, dict):
    R = len(m)-1
    C = len(m[0])-1
    current = start
    direction = dir
    while str(current) + str(direction) not in dict.keys():
        key = str(current) + str(direction)
        x,y = current
        if x < 0 or x > R or y < 0 or y > C:
            break    
        dict[key] = x,y
        c = m[x][y]
        if c == "/" or c == "\\":
            direction = new_dir(c,direction)
            current = move(current, direction)
        elif (direction == 0 or direction == 2) and c == "|":
            traverse_path(m, move(current,1),1, dict)
            traverse_path(m, move(current,3),3, dict)
        elif (direction == 3 or direction == 1) and c == "-":
            traverse_path(m, move(current,0),0, dict)
            traverse_path(m, move(current,2),2, dict)
        else:
            current = move(current, direction)

def p1(puzzle):
    m = parse(puzzle)
    dict = {}
    start = 0,0
    traverse_path(m,start,0,dict)
    return score(m,dict)


def score(m, dict):
    k = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if (i,j) in dict.values():
                k += 1
    return k

def p2(puzzle):
    m = parse(puzzle)
    dict = {}
    values = []
    for i in range(len(m)-1):
        dict = {}
        start = 0,i
        traverse_path(m, start, 1, dict)
        values.append(score(m, dict))
        dict.clear()
        start = len(m)-1,i
        traverse_path(m, start, 3, dict)
        values.append(score(m, dict))
        dict.clear()
        start = i,0
        traverse_path(m, start, 0, dict)
        values.append(score(m, dict))
        dict.clear()
        start = i,len(m)-1
        traverse_path(m, start, 0, dict)
        values.append(score(m, dict))
    return max(values)

print(p1(lines),p2(lines))

print("--- %s seconds ---" % (time.time() - start_time))




""" 

m = parse(lines)
R = len(m)-1
C = len(m[0])-1

dick = {}

def traverse(start, direction):
    x,y = start 
    if x < 0 or x > R or y < 0 or y > C:
        return []
    
    if (start, direction) in dick:
        return dick[(start,direction)]
    
    c = m[x][y]
    if c == "/" or c == "\\":
        direction = new_dir(c,direction)
        result = traverse(move(start,direction), direction) + [start]
        dick[(start,direction)] = result
        return result
    
    elif (direction == 0 or direction == 2) and c == "|":
        result_up = traverse(move(start,3),3) + [start]
        result_down = traverse(move(start,1),1)
        result = list(set(result_up + result_down))
        dick[((start,direction))] = result
        return result
    
    elif (direction == 3 or direction == 1) and c == "-":
        result_right = traverse(move(start,0),0) + [start]
        result_left = traverse(move(start,2),2)
        result = list(set(result_left + result_right))
        dick[((start,direction))] = result
        return result
    else:
        result = traverse(move(start, direction), direction) + [start]
        dick[(start,direction)] = result
        return result """
