import time
start_time = time.time()
import uf
import math

dick = {
    "|": ["north", "south"],
    "-": ["west", "east"],
    "L": ["north", "east"],
    "7": ["west", "south"],
    "J": ["north", "west"],
    "F": ["south", "east"],
    "S": ["south", "east", "west", "north"],
    ".": [],
}


lines = uf.read_lines("../in/10.in")[:-1]
tests = uf.read_lines("../test/10.in")[:-1]

class Graph: #Chat gpt's graf
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].append(vertex2)

    def display_graph(self):
        for vertex, neighbors in self.vertices.items():
            print(f"{vertex}: {neighbors}")

g = Graph()

def connection(c1, c2):
    l1 = dick[c1]
    l2 = dick[c2]
    for item in l1:
        if item in l2:
            return True
    return False

def count_changes(j, line, r):
    t = 0
    for i in range(0, j):
        if line[i] in "JL|S" and (r,i) in g.vertices.keys():
            t += 1
    if t % 2 == 1:
        return 1
    return 0

def findLoop(matrix):
    arr = [list(row) for row in matrix]
    R = len(matrix)
    C = len(matrix[0])
    s1 = 0
    s2 = 0
    for i, line in enumerate(matrix):
        for j, c in enumerate(line):
            if c == "S":
                s1 = i
                s2 = j
    c1 = s1
    c2 = s2
    
    while True:
        if c1+1 < R and "north" in dick[matrix[c1+1][c2]] and "south" in dick[matrix[c1][c2]] and (not (c1+1,c2) in g.vertices.keys()):
            c1 += 1
        elif c1-1 >= 0 and "south" in dick[matrix[c1-1][c2]] and "north" in dick[matrix[c1][c2]] and (not (c1-1,c2) in g.vertices.keys()):
            c1 -= 1
        elif c2+1 < C and "west" in dick[matrix[c1][c2+1]] and "east" in dick[matrix[c1][c2]] and (not (c1,c2+1) in g.vertices.keys()):
            c2 += 1
        elif c2-1 >= 0 and "east" in dick[matrix[c1][c2-1]] and "west" in dick[matrix[c1][c2]] and (not (c1,c2-1) in g.vertices.keys()):
            c2 -= 1
        g.add_vertex((c1,c2))
        if (c1 == s1 and c2 == s2):
            break

    total = 0
    for i, line in enumerate(matrix):
        for j, c in enumerate(line):
            if not (i,j) in g.vertices.keys():
                total += count_changes(j,line,i)
    return len(g.vertices.keys()) // 2, total
        
res, total = findLoop(lines)

print(res, total)
print("--- %s seconds ---" % (time.time() - start_time))
