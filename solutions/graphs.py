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
            self.vertices[vertex2].append((vertex1, w))     


    def display_graph(self):
        for vertex, neighbors in self.vertices.items():
            print(f"{vertex}: {neighbors}")

def shortest_path(graph: Graph, src, dst):
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
    q.put((0, node, node))
    while not q.empty():
        weight, src, dst = q.get()
        if src not in s.keys():
            s[src] = weight, dst
        else:
            continue
        for node, w in graph.vertices[src]:
            if node not in s.keys():
                q.put((w+weight, node, src))
    return s

g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")
g.add_vertex("F")
g.add_vertex("G")

g.add_edge("A","B",15)
g.add_edge("A","C",53) 
g.add_edge("B","C",40) 
g.add_edge("B","D",46) 
g.add_edge("C","E",31) 
g.add_edge("C","G",17) 
g.add_edge("E","G",29) 
g.add_edge("E","D",3)
g.add_edge("F","G",40) 
g.add_edge("F","D",11) 
g.add_edge("F","E",8) 

g.display_graph()

print(shortest_path(g,"A","G"))