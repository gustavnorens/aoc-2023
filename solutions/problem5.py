import uf
import time
start_time = time.time()

input = uf.read_lines("../in/input5.txt")[:-1]
test = uf.read_lines("../test/test5.in")[:-1]

def p1(input):
    seeds, maps = parse(input)
    seeds = list(zip(seeds, [False] * len(seeds)))
    locations = convert(seeds, maps)
    m = min(seeds)
    
    return m[0]

def p2(input):
    seeds, maps = parse(input)
    seed_range = []
    for i in range(0,len(seeds),2):
        for j in range(seeds[i], seeds[i]+seeds[i+1],3000):
            seed_range.append(j)
    seed_range = list(zip(seed_range, [False] * len(seed_range)))
    locations = convert(seed_range.copy(), maps)
    m = min(locations)
    k = locations.index(m)

    print(k)

    approx = seed_range[k][0]
    seed_range = []
    for i in range(approx-100000, approx+100000):
        seed_range.append(i)
    seed_range = list(zip(seed_range, [False] * len(seed_range)))
    locations = convert(seed_range, maps)
    m = min(locations)
    return m[0]


def convert(s, maps):
    for m in maps:
        m = m[1:]
        for i, (seed, b) in enumerate(s):
            s[i] = seed, False
        for i, line in enumerate(m):
            dest, source, length = list(map(int,line.split()))
            for j, (seed,b) in enumerate(s):
                if source <= seed < source+length and not b:
                    s[j] = (seed+dest-source, True)
    return s

def parse(input):
    lists = []
    last = 0
    input.append("")
    for i, line in enumerate(input):
         if line == "":
             if last != 0:
                 lists.append(input[last+1:i])
             else:
                 lists.append(input[last:i])
             last = i
    seeds, rest = lists[0], lists[1:]
    seeds = seeds[0][7:]
    seeds = seeds.split()
    seeds = list(map(int,seeds))
    return seeds, rest

print(p1(input))
print(p2(input)) #Probably doesnt always work.

print("--- %s seconds ---" % (time.time() - start_time))



    


