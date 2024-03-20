class DirectedGraph:
    def __init__(self):
        self.adjacency_list = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
    
    def add_edge(self, from_vertex, to_vertex):
        # Adds an edge from from_vertex to to_vertex
        if from_vertex in self.adjacency_list:
            self.adjacency_list[from_vertex].append(to_vertex)
    
    def display(self):
        for vertex, edges in self.adjacency_list.items():
            print(f"{vertex} -> {', '.join(edges)}")

class UndirectedGraph:
    def __init__(self):
        self.adjacency_list = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        # Adds an edge between vertex1 and vertex2
        if vertex1 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
        if vertex2 in self.adjacency_list:
            self.adjacency_list[vertex2].append(vertex1)
    
    def display(self):
        for vertex, edges in self.adjacency_list.items():
            print(f"{vertex} -> {', '.join(edges)}")

# Directed Graph Example
print("Directed Graph:")
d_graph = DirectedGraph()
d_graph.add_vertex('A')
d_graph.add_vertex('B')
d_graph.add_vertex('C')
d_graph.add_edge('A', 'B')  # A -> B
d_graph.add_edge('A', 'C')
d_graph.display()

# Undirected Graph Example
print("\nUndirected Graph:")
u_graph = UndirectedGraph()
u_graph.add_vertex('A')
u_graph.add_vertex('B')
u_graph.add_vertex('C')
u_graph.add_edge('A', 'B')  # A -- B
u_graph.add_edge('A', 'C')
u_graph.display()