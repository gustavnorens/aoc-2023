import uf
import time
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
    
    return list(zip(times, distances)), time, distance

def p1(lines):
    parsed,_,_ = parse(lines)
    total = 1
    for time, dist in parsed:
        counter = 0
        for i in range(0, time):
            if i*(time-i) > dist:
                counter += 1
        total *= counter
        print(counter)
    return total

print(p1(lines))

def p2(lines):
    _, time, dst = parse(lines)
    counter = 0
    for i in range(0, int(time)):
        print(i)
        print(time)
        if i*(int(time)-i) > int(dst):
            counter += 1
    return total

print(p2(lines))
