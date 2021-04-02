class AdjacentNode:
    def __init__(self, vertex):
        self.vertex = vertex
        self.next = None

class BidirectionalSearch:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [None] * self.vertices
        self.src_queue = list()
        self.dest_queue = list()

        self.src_visited = [False] * self.vertices  # Initializing source and destination visited nodes as False
        self.dest_visited = [False] * self.vertices

        self.src_parent = [None] * self.vertices # Initializing source and destination
        self.dest_parent = [None] * self.vertices  # parent nodes

    # Function for adding undirected edge
    def add_edge(self, src, dest):
        node = AdjacentNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node
        # Since graph is undirected add destination to source
        node = AdjacentNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    # Function for Breadth First Search
    def bfs(self, direction='forward'):
        if direction == 'forward':
            # !!-------------------------------BFS in forward direction
            current = self.src_queue.pop(0)
            connected_node = self.graph[current]

            while connected_node:
                vertex = connected_node.vertex

                if not self.src_visited[vertex]:
                    self.src_queue.append(vertex)
                    self.src_visited[vertex] = True
                    self.src_parent[vertex] = current

                connected_node = connected_node.next
            # !!---------------------------------------------------------
        else:
            # !!-----------------------------------BFS in backward direction
            current = self.dest_queue.pop(0)
            connected_node = self.graph[current]

            while connected_node:
                vertex = connected_node.vertex

                if not self.dest_visited[vertex]:
                    self.dest_queue.append(vertex)
                    self.dest_visited[vertex] = True
                    self.dest_parent[vertex] = current

                connected_node = connected_node.next
            # !!-----------------------------------------------------------

    # Check for intersecting vertex
    def is_intersecting(self):

        for i in range(self.vertices):
            if (self.src_visited[i] and
                    self.dest_visited[i]):
                return i
        return -1

    # Print the path from source to target
    def print_path(self, intersecting_node,
                   src, dest):
        # Print final path from source to destination
        path = list()
        path.append(intersecting_node)
        i = intersecting_node

        while i != src:
            path.append(self.src_parent[i])
            i = self.src_parent[i]

        path = path[::-1]
        i = intersecting_node

        while i != dest:
            path.append(self.dest_parent[i])
            i = self.dest_parent[i]

        print("##!!-----------------Path----------------!!##")
        path = list(map(str, path))

        print(' '.join(path))

    # Function for bidirectional searching
    def bidirectional_search(self, src, dest):

        # Add source to queue and mark visited as True and add its parent as -1
        self.src_queue.append(src)
        self.src_visited[src] = True
        self.src_parent[src] = -1
        # Add destination to queue and mark visited as True and add its parent as -1
        self.dest_queue.append(dest)
        self.dest_visited[dest] = True
        self.dest_parent[dest] = -1

        while self.src_queue and self.dest_queue:

            # BFS in forward direction from Source Vertex
            self.bfs(direction='forward')

            # BFS in reverse direction from Destination Vertex
            self.bfs(direction='backward')

            # Check for intersecting vertex
            intersecting_node = self.is_intersecting()

            # If intersecting vertex exists then path from source to destination exists
            if intersecting_node != -1:
                print(f"!---------Path exists between {src} and {dest}-------------!")
                print(f"Intersection at node is : {intersecting_node}")
                self.print_path(intersecting_node,
                                src, dest)
                exit(0)
        return -1
print("\n\t\tBidirectional Search ")

print("!!---------------Graph-----------------!!")
print("(1 , 2)")
print("(1 , 3)")
print("(2 , 4)")
print("(2 , 5)")
print("(3 , 6)")
print("(3 , 7)")

src =int(input("Enter the source Node : "))
dest =int(input("Enter the destination Node : "))

n = 8
graph = BidirectionalSearch(n)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(2, 5)
graph.add_edge(3, 6)
graph.add_edge(3, 7)


out = graph.bidirectional_search(src, dest)

if out == -1:
        print(f"Path does not exist between {src} and {dest}")

