class Vertex:

    def __init__(self, value):
        self.value = value
        self.neighbours = {}

    def __repr__(self):
        return str(self.value)


class Graph:

    def __init__(self):
        self.vertices = {}

    def find(self, value):
        return self.vertices.get(value)

    def add_vertex(self, value):
        if not self.find(value):
            self.vertices[value] = Vertex(value)
        else:
            print(value, "already exist")

    def add_edge(self, source, target, weight=1):
        source_v = self.find(source)
        target_v = self.find(target)

        if source_v and target_v:
            source_v.neighbours[target_v] = weight
            target_v.neighbours[source_v] = weight
        else:
            print("Some of", source, target, "are missing")

    def display(self):
        for vertex in self.vertices.values():
            print(vertex, ":", vertex.neighbours)


if __name__ == "__main__":

    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")

    graph.add_edge("A", "B", 5)
    graph.add_edge("D", "C")

    graph.display()

