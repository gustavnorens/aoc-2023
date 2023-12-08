import time
start_time = time.time()
import uf
from collections import Counter
import math

lines = uf.read_lines("../in/8.in")[:-1]
tests = uf.read_lines("../test/8.in")[:-1]

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

def parse(lines):
    ins = lines[0]

    nodes = []
    edges = []
    
    for line in lines[2:]:
        node, edge = line.split(" = ")
        edges.append(edge[1:-1].split(", "))
        nodes.append(node)
    return ins, nodes, edges

def steps(node, ins, g, end):
    i = 0
    while not node.endswith(end):
        choice = ins[i % len(ins)]
        if choice == "L":
            node = g.vertices[node][0]
        elif choice == "R":
            node = g.vertices[node][1]
        i += 1
    return i

def solve(lines):
    ins, nodes, edges = parse(lines)
    g = Graph()
    for node in nodes:
        g.add_vertex(node)
    for i, node in enumerate(nodes):
        g.add_edge(node, edges[i][0])
        g.add_edge(node, edges[i][1])
    p1 = steps("AAA", ins, g, "ZZZ")

    aaa = [node for node in nodes if node.endswith("A")]
    
    result = ([steps(node, ins, g, "Z") for node in aaa])
    p2 = math.lcm(*result)
    return p1, p2

print(solve(lines))
print("--- %s seconds ---" % (time.time() - start_time))
