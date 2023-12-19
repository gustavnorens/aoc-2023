import time
start_time = time.time()
import uf

lines = uf.read_lines("../in/day17.input")[:-1]
tests = uf.read_lines("../test/17-2.in")[:-1]

from queue import PriorityQueue


def opposite(i):
    return (i + 2) % 4

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []

    def add_edge(self, vertex1, vertex2, w):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].append((vertex2,w))

    def display_graph(self):
        for vertex, neighbors in self.vertices.items():
            print(f"{vertex}: {neighbors}")
            
def parse(puzzle):
    g = Graph()
    for i, row in enumerate(puzzle):
        for j, c in enumerate(puzzle):            
            g.add_vertex((i,j))
            if i + 1 >= 0 and i + 1 < len(puzzle):
                g.add_vertex((i+1,j))
                g.add_edge((i,j), (i+1, j), int(puzzle[i+1][j]))
            if i - 1 >= 0 and i - 1 < len(puzzle):
                g.add_vertex((i-1,j))
                g.add_edge((i,j), (i-1, j), int(puzzle[i-1][j]))
            if j + 1 >= 0 and j + 1 < len(puzzle):
                g.add_vertex((i,j+1))
                g.add_edge((i,j), (i, j+1), int(puzzle[i][j+1]))
            if j - 1 >= 0 and j - 1 < len(puzzle):
                g.add_vertex((i,j-1))   
                g.add_edge((i,j), (i,j-1), int(puzzle[i][j-1]))
    return g

def dijk_p1(graph, start, end):
    q = PriorityQueue()
    v = {}
    q.put((0, start, -1, 0))
    while not q.empty():
        weight, dst, direc, steps = q.get()
        key = dst, direc, steps
        if dst == end and steps <= 3:
            return weight
        if key in v:
            continue
        v[key] = 0
        if steps <= 3:
            for node, w in graph[dst]:
                d = dir(dst,node)                 
                if direc == d:
                    new_steps = steps + 1
                else:
                    new_steps = 1
                if d != opposite(direc):
                    q.put((w+weight, node, d, new_steps))
    return None

def dijk_p2(graph, start, end):
    q = PriorityQueue()
    v = {}
    q.put((0, start, -1, 0))
    while not q.empty():
        weight, dst, direc, steps = q.get()
        key = dst, direc, steps
        if dst == end and steps >= 4:
            return weight 
        if key in v:
            continue
        v[key] = 0
        if steps <= 10:
            for node, w in graph[dst]:
                d = dir(dst,node)
                if direc == d:
                    q.put((w+weight, node, d, steps+1))
                elif steps >= 4 or direc == -1 and opposite(direc):
                    q.put((w+weight, node, d, 1))
    return None

def dir(node1, node2):
    x,y = node1
    i,j = node2
    if x-i == 1 and y-j == 0:
        return 3
    if x-i == -1 and y-j == 0:
        return 1
    if x-i == 0 and y-j == 1:
        return 0
    if x-i == 0 and y-j == -1:
        return 2

def solve(puzzle):
    R = len(puzzle)-1
    C = len(puzzle[0])-1
    g = parse(puzzle)
    verts = g.vertices
    p1 = 0
    p2 = 0
    p1 = dijk_p1(verts,(0,0), (R,C))
    p2 = dijk_p2(verts,(0,0), (R,C))
    return p1, p2

print(solve(lines))

print("--- %s seconds ---" % (time.time() - start_time))


