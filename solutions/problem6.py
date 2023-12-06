import uf
import time
import numpy as np
import math
start_time = time.time()

lines = uf.read_lines("../in/6.in")[:-1]
test = uf.read_lines("../test/6.in")[:-1]

def parse(lines):
    l = []
    for i,line in enumerate(lines):
        if line != "":
            _, content = line.split(":")
            l.append(content.split())
    times = map(int,l[0])
    distances = map(int,l[1])

    time = "".join(l[0])
    distance = "".join(l[1])
    
    return list(zip(times, distances)), int(time), int(distance)

def p1(lines):
    parsed,_,_ = parse(lines)
    total = 1
    for time, dist in parsed:
            coeffs = [-1,time,-dist]
            roots = list(map(math.ceil,np.roots(coeffs)))
            total *= roots[0] - roots[1]
    return total

def p2(lines):
    _, time, dst = parse(lines)
    coeffs = [-1,time,-dst]
    roots = list(map(math.ceil,np.roots(coeffs)))
    return roots[0] - roots[1]

print(p1(lines))
print(p2(lines))

print("--- %s seconds ---" % (time.time() - start_time))     

