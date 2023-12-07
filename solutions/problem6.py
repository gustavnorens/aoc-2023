import time
start_time = time.time()
import uf


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
            rs = list(map(lambda x: x // 1,roots(*coeffs)))
            total *= rs[0] - rs[1]
    return int(total)

def p2(lines):
    _, time, dst = parse(lines)
    coeff = [-1,time,-dst]
    rs = list(map(lambda x: x // 1, roots(*coeff)))
    return int(max(rs[0], rs[1]) - min(rs[0], rs[1]))

def roots(a,b,c):
    first = -b / (2 *a)
    second = ((b**2-4*a*c)**0.5) / (2*a)
    return (first + second, first - second)

print(p1(lines))
print(p2(lines))

print("--- %s seconds ---" % (time.time() - start_time))

