class Vertex:

    def __init__(self, value):
        self.value = value
        self.neighbours = []

    def __repr__(self):
        return str(self.value)


class Graph:

    def __init__(self):
        self.vertices = []

    def find(self, value):
        for vertex in self.vertices:
            if vertex.value == value:
                return vertex
        return None

    def add_vertex(self, value):
        if not self.find(value):
            self.vertices.append(Vertex(value))
        else:
            print(value, "already exist")

    def add_edge(self, source, target):
        source_v = self.find(source)
        target_v = self.find(target)

        if source_v and target_v:
            source_v.neighbours.append(target_v)
            target_v.neighbours.append(source_v)
        else:
            print("Some of", source, target, "are missing")

    def display(self):
        for vertex in self.vertices:
            print(vertex, ":", vertex.neighbours)

    def depth_first_trev(self, source=None):
        if not source:
            vertex = self.vertices[0]
        else:
            vertex = self.find(source)

        stack = list()
        visited = set()

        stack.append(vertex)
        visited.add(vertex)

        while len(stack) > 0:
            vertex = stack.pop()
            print(vertex)

            for neighbour in vertex.neighbours:
                if neighbour not in visited:
                    visited.add(neighbour)
                    stack.append(neighbour)

    def breadth_first_trev(self, source=None):
        if not source:
            vertex = self.vertices[0]
        else:
            vertex = self.find(source)

        queue = list()
        visited = set()

        queue.append(vertex)
        visited.add(vertex)

        while len(queue) > 0:
            vertex = queue.pop(0)

            print(vertex)

            for neighbour in vertex.neighbours:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

    def breadth_first_search(self, source, target):
        vertex = self.find(source)

        queue = list()
        visited = set()

        queue.append(vertex)
        visited.add(vertex)

        while len(queue) > 0:
            vertex = queue.pop(0)

            if vertex.value == target:
                return True

            for neighbour in vertex.neighbours:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

        return False

    def breadth_first_search_cost(self, source, target):
        vertex = self.find(source)

        level = 0

        queue = list()
        visited = set()

        queue.append(vertex)
        queue.append(None)
        visited.add(vertex)

        while len(queue) > 1:
            vertex = queue.pop(0)

            if vertex is None:
                level += 1
                queue.append(None)
                continue

            if vertex.value == target:
                return level

            for neighbour in vertex.neighbours:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

        return -1

    def breadth_first_search_level(self, source):
        vertex = self.find(source)

        level = 0

        queue = list()
        visited = set()

        queue.append(vertex)
        queue.append(None)
        visited.add(vertex)

        while len(queue) > 1:
            vertex = queue.pop(0)

            if vertex is None:
                level += 1
                queue.append(None)
                continue

            print(vertex, level)

            for neighbour in vertex.neighbours:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)


    def depth_first_search(self, source, target):

        vertex = self.find(source)

        stack = list()
        visited = set()

        stack.append(vertex)
        visited.add(vertex)

        while len(stack) > 0:
            vertex = stack.pop()

            if vertex.value == target:
                return True

            for neighbour in vertex.neighbours:
                if neighbour not in visited:
                    visited.add(neighbour)
                    stack.append(neighbour)

        return False


if __name__ == "__main__":

    graph = Graph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)

    graph.add_edge(1, 2)
    graph.add_edge(3, 2)
    graph.add_edge(4, 3)
    graph.add_edge(4, 2)

    print(graph.breadth_first_search_level(1))
