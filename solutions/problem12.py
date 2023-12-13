import time
start_time = time.time()
from queue import PriorityQueue
import uf
from graphs import Graph,DiGraph
from itertools import permutations, combinations

lines = uf.read_lines("../in/12.in")[:-1]
tests = uf.read_lines("../test/12.in")[:-1]

def parse(input):
    input = [line for line in input if "-" not in line]
    games, numbers = list(zip(*map(str.split, input)))
    numbers = [list(reversed(list(map(int,num.split(","))))) for num in numbers]
    new_games = []
    for game in games:
        new = ".".join([split for split in game.split(".") if split != ""])
        new_games.append(new)
    return new_games, numbers

def parse2(input):
    input = [line for line in input if "-" not in line]
    
    games, numbers = list(zip(*map(str.split, input)))
    games = [((game + "?")*2)[:-1] for game in games]
    numbers = [list(reversed(list(map(int,num.split(",")))*2)) for num in numbers] 
    new_games = []
    for game in games:
        new = ".".join([split for split in game.split(".") if split != ""])
        new_games.append(new)
    return new_games, numbers
    
def score(game, nums):
    new = [num for num in nums]
    g = game
    while new:
        current = new.pop()
        counter = 0
        start = 0
        for i,c in enumerate(g):
            if c == "#":
                if counter == 0:
                    start = i
                counter += 1
            if c != "#" or i == len(g) - 1:
                if counter == current:
                    g = g[i+1:]
                    break
                counter = 0
        else:
            return 0
    return 1

def from_game(game, nums):
    total = sum(nums)
    tqms = game.count("?")
    thsh = game.count("#")
    dots = tqms+thsh - total
    hsh = tqms-dots

    words = perms(".", "#", dots, hsh)
    l = []
    for word in words:
        k = 0
        new = list(game)
        for i, c in enumerate(new):
            if c == "?":
                new[i] = word[k]
                k += 1
        l.append("".join(new))
    l = [score(game,nums) for game in l]
    print(sum(l))
    return sum(l)

def perms(a,b,ca,cb):
    combs = combinations(range(ca+cb),ca)
    res = []
    for nums in combs:
        s = ["#"]*(cb+ca)
        for i in nums:
            s[i] = "."
        res.append("".join(s))
    return res

def solve(input):
    games, numbers = parse2(input)
    res = zip(games, numbers)
    return sum([from_game(game,nums) for game,nums in res])

print(solve(lines))

# game, numbers = parse2(lines)
# print(from_game(game[1],numbers[1]))


def shortest_past(graph: Graph, src, dst):
    s = dijkstra(graph, src)
    stack = []
    res = []
    cost = s[dst][0]
    while dst != src:
        stack.append(dst)
        dst = s[dst][1]
    stack.append(dst)
    while stack:
        res.append(stack.pop())
    return cost, res

def dijkstra(graph: Graph, node):
    q = PriorityQueue()
    s = {}
    q.put((0,node,""))
    while not q.empty():
       weight, src, dst = q.get()
       if src not in s.keys():
               s[src] = weight, dst
       for node, w in graph.vertices[src]:
           if node not in s.keys():
               q.put((w+weight, node, src))
    return s

print("--- %s seconds ---" % (time.time() - start_time))
