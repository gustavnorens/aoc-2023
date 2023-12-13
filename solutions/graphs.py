from queue import PriorityQueue

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []

    def add_edge(self, vertex1, vertex2, w):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].append((vertex2,w))
            self.vertices[vertex2].append((vertex1, w))

    def display_graph(self):
        for vertex, neighbors in self.vertices.items():
            print(f"{vertex}: {neighbors}")


class DiGraph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []

    def add_edge(self, vertex1, vertex2, w):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].append((vertex2, w))


    def display_graph(self):
        for vertex, neighbors in self.vertices.items():
            print(f"{vertex}: {neighbors}")



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
