import time
start_time = time.time()
import uf

lines = uf.read_lines("../in/7.in")[:-1]
tests = uf.read_lines("../test/7.in")[:-1]

def parse(lines):
    res = []
    for line in lines:
            res.append(line.split())
    return res
    
def multiply(pair):
    return pair[0] * pair[1]

def score_p1(pair):
    scores = sorted([pair[0].count(c) for c in set(pair[0])], reverse=True)
    ind = int(pair[0].replace("A", "E").replace("K", "D").replace("Q", "C").replace("J","B").replace("T","A"), 16)
    return (scores[:2], ind), pair[1]

def score_p2(pair):
    js = pair[0].count("J")
    score = sorted([pair[0].count(c) for c in set(pair[0].replace("J", ""))]+[0], reverse=True)
    score[0] += js
    ind = int(pair[0].replace("A", "E").replace("K", "D").replace("Q", "C").replace("J","1").replace("T","A"), 16)
    return (score[:2], ind), pair[1]

def solve(lines):
    parsed = parse(lines)
    _,res1 = zip(*sorted(list(map(score_p1, parsed))))
    _,res2 = zip(*sorted(list(map(score_p2, parsed))))
    res1 = list(map(int, res1))
    res2 = list(map(int, res2))
    return sum(map(multiply,zip(res2, range(1,len(res2) + 1)))),sum(map(multiply,zip(res1,range(1,len(res1) + 1))))

p2, p1 = solve(lines)

print(p1)
print(p2)

print("--- %s seconds ---" % (time.time() - start_time))
