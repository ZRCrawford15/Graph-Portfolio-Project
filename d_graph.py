# Course: CS261 - Data Structures
# Author:
# Assignment:
# Description:


import heapq
from collections import deque


class DirectedGraph:
    """
    Class to implement directed weighted graph
    - duplicate edges not allowed
    - loops not allowed
    - only positive edge weights
    - vertex names are integers
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency matrix
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.v_count = 0
        self.adj_matrix = []

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            v_count = 0
            for u, v, _ in start_edges:
                v_count = max(v_count, u, v)
            for _ in range(v_count + 1):
                self.add_vertex()
            for u, v, weight in start_edges:
                self.add_edge(u, v, weight)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if self.v_count == 0:
            return 'EMPTY GRAPH\n'
        out = '   |'
        out += ' '.join(['{:2}'.format(i) for i in range(self.v_count)]) + '\n'
        out += '-' * (self.v_count * 3 + 3) + '\n'
        for i in range(self.v_count):
            row = self.adj_matrix[i]
            out += '{:2} |'.format(i)
            out += ' '.join(['{:2}'.format(w) for w in row]) + '\n'
        out = f"GRAPH ({self.v_count} vertices):\n{out}"
        return out

    # ------------------------------------------------------------------ #

    def add_vertex(self) -> int:
        """
        Adds a new vertex to the graph. Inserted vertex will be assigned
        a reference index integer. First vertex is index 0.
        Return: The total number of vertices in the graph
        """

        # add new row with the number of columns
        self.adj_matrix.append([0] * self.v_count)

        # append new column to each row

        for row in self.adj_matrix:
            row.append(0)


        self.v_count += 1

        return self.v_count

    def add_edge(self, src: int, dst: int, weight=1) -> None:
        """
        Adds a new edge to the graph. Connecting two verticies
        with a positive weight
        """

        # invalid vertex
        if src > len(self.adj_matrix) - 1 or dst > len(self.adj_matrix[0]) - 1:
            return

        # same vertex
        if src == dst:
            return

        # invalid weight
        if weight < 1:
            return

        self.adj_matrix[src][dst] = weight

        return

    def remove_edge(self, src: int, dst: int) -> None:
        """
        Removes an edge between two vertices.
        """

        rows = len(self.adj_matrix)
        columns = len(self.adj_matrix[0])

        row_valid_index = rows - 1
        column_valid_index = columns - 1

        if src < 0 or dst < 0:
            print(f"SRC: {src}, DST: {dst}")
            print("Invalid Index, cannot be less than 0")
            return

        if src > row_valid_index or dst > column_valid_index:
            print(f"SRC: {src}, DST: {dst}")

            print("Invalid Index")
            return

        self.adj_matrix[src][dst] = 0

        return

    def get_vertices(self) -> []:
        """
        Gets the vertices in the graph
        """

        vertices = []

        for count, value in enumerate(self.adj_matrix):
            vertices.append(count)

        return vertices



    def get_edges(self) -> []:
        """
        Gets the edges in the graph
        """

        edges = []

        for row in range(len(self.adj_matrix)):
            for column in range(len(self.adj_matrix[row])):
                weight = self.adj_matrix[row][column]
                if weight > 0:
                    edges.append((row, column, weight))

        return edges

    def is_valid_path(self, path: []) -> bool:
        """
       Checks if a given path is valid in the graph
        """

        # starting position is the row
        # ending is row + column
        # ending must be > 0

        # counter = 0
        # path_length = len(path) - 1
        # while counter < path_length - 1:
        for i in range(len(path) - 1):
            # check vertex from beginning to end without going out of bounds
            current = path[i]
            next_vertex = path[i + 1]
            # counter += 1

            test = self.adj_matrix[current][next_vertex]
            if self.adj_matrix[current][next_vertex] > 0:
                continue
            else:
                return False

        return True

    def dfs(self, v_start, v_end=None) -> []:
        """
        Depth first search that returns a list
        of vertices in the order they were visited during the search.
        If the starting vertex is not in the graph an empty list is returned
        Param v_start: starting search node
        Param v_end: ending search node
        Return: list of traversed nodes in order of visit
        """

        # Starting node is not in the graph
        if v_start not in range(len(self.adj_matrix)):
            return []

        # 1) initialize hash table of vertices
        visited = {}
        matrix = self.adj_matrix
        for vertex in range(len(matrix)):
            visited[vertex] = False

        # initialize empty stack
        stack = []
        traveled_list = []
        stack.append(v_start)

        while len(stack) > 0:
            # pop top element
            top = stack.pop()

            if top == v_end:
                traveled_list.append(top)
                return

            elif top != v_end and not visited[top]:
                # appended traveled list
                traveled_list.append(top)
                # set vertex as visited
                visited[top] = True
                # add each successor of vertex to the stack
                successors = self.adj_matrix[top]

                counter = len(successors)
                for vertex in range(len(successors), 0, -1):
                    counter -= 1
                    if successors[counter] > 0:
                        stack.append(counter)

        return traveled_list


    def bfs(self, v_start, v_end=None) -> []:
        """
        Breadth-first search that returns a list
        of vertices in the order they were visited during the search.
        If the starting vertex is not in the graph an empty list is returned
        Param v_start: starting search node
        Param v_end: ending search node
        Return: list of traversed nodes in order of visit
        """

        # Starting node is not in the graph
        if v_start not in range(len(self.adj_matrix)):
            return []

        # 1) initialize hash table of vertices
        visited = {}
        matrix = self.adj_matrix
        for vertex in range(len(matrix)):
            visited[vertex] = False

        # initialize empty stack
        queue = []
        traveled_list = []
        queue.append(v_start)

        while len(queue) > 0:
            front = queue.pop(0)
            if visited[front]:
                continue
            visited[front] = True
            if front == v_end:
                traveled_list.append(front)
                break

            successors = self.adj_matrix[front]
            counter = 0
            traveled_list.append(front)
            for vertex in range(len(successors)):
                if not visited[counter] and successors[counter] > 0:
                    queue.append(counter)
                counter += 1

        return traveled_list

    def has_cycle(self):
        """
        TODO: Write this implementation
        """
        # Think of clever solution
        # For all nodes
            # 1) pick any node and start searching
            # 2) see where end is
            # 3) check if end is same as starting node
        visited = {}
        matrix = self.adj_matrix
        for vertex in range(len(matrix)):
            visited[vertex] = False

        rec_stack = {}
        for vertex in range(len(matrix)):
            rec_stack[vertex] = False

        for i in range(len(self.adj_matrix)):
            if not visited[i]:
                if self.has_cycle_helper(i, visited, rec_stack):
                    return True

        return False


    def has_cycle_helper(self, vertex, visited, rec_stack):

        visited[vertex] = True

        # current path of visited nodes to reference
        # back to check for a cycle
        rec_stack[vertex] = True

        successors = self.adj_matrix[vertex]
        counter = -1

        # check each child of the vertex
        for child in successors:
            counter += 1
            # if the vertex is not visited and has a connected edge
            # check its successors and children for a vertex that
            # has already been visited in the path. Therefore
            # finding a cycle
            if not visited[counter] and child > 0:
                if self.has_cycle_helper(counter, visited, rec_stack):
                    return True
            elif rec_stack[counter] and child > 0:
                return True

        rec_stack[vertex] = False
        return False




    def dijkstra(self, src: int) -> []:
        """
        TODO: Write this implementation
        """
        # Start at a vertex
        # check every edge and calculate cost -> list
            #[0: 15, 1: 20, 2: 3] - find minumum cost
        # for each neighbor, evaluate all of its neighbors (dfs)

        # initialize empty hash table of visited vertices
        visited = {}
        matrix = self.adj_matrix
        for vertex in range(len(matrix)):
            visited[vertex] = float('inf')

        visited2 = {}
        for vertex in range(len(matrix)):
            visited2[vertex] = False

        # first node distance is 0
        visited[src] = 0

        # initialize first value in queue
        queue = [src]
        returned_list = []
        priority_queue = []
        heapq.heapify(priority_queue)

        while len(queue) > 0:
            vertex = queue.pop(0)
            d = visited[vertex]
            if d == float('inf'):
                returned_list.append(float('inf'))
                continue
            for i in range(len(self.adj_matrix[vertex])):
                # not visited if value is infinity
                if visited[i] == float('inf'):
                    if self.adj_matrix[vertex][i] > 0:
                        # add v to visited with cost of edge
                        visited[i] = self.adj_matrix[vertex][i]

                        d2 = 0
                        # for each successor of vertex
                        # if there is an edge let d2 = cost
                        if self.adj_matrix[vertex][i] > 0:
                            d2 = self.adj_matrix[vertex][i]
                            # add d with d2
                            visited[i] = d2 + d
                            # insert successor with distance into priority queue with updated distance value
                            heapq.heappush(priority_queue, self.adj_matrix[vertex][i])

            # Gets the vertex associated with the lowest edge to append
            # to the priority queue
            # TODO: This did nothing to help solve shortest path
            # TODO: Still picking lowest node index
            key_list = list(visited.keys())
            value_list = list(visited.values())
            #
            for i in range(len(value_list)):
                if visited[i] != float('inf') and visited[i] > 0:
                    if not visited2[i]:
                        queue.append(i)
                        visited2[i] = True

            priority_queue = []
            heapq.heapify(priority_queue)


        # append cost of each visited vertex to final list

        for i in range(len(visited)):
            returned_list.append(visited[i])


        return returned_list









if __name__ == '__main__':

    # print("\nPDF - method add_vertex() / add_edge example 1")
    # print("----------------------------------------------")
    # g = DirectedGraph()
    # print(g)
    # for _ in range(5):
    #     g.add_vertex()
    # print(g)
    #
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # for src, dst, weight in edges:
    #     g.add_edge(src, dst, weight)
    # print(g)
    #
    # g.remove_edge(6, 9)
    #
    #
    # print("\nPDF - method get_edges() example 1")
    # print("----------------------------------")
    # g = DirectedGraph()
    # print(g.get_edges(), g.get_vertices(), sep='\n')
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # g = DirectedGraph(edges)
    # print(g.get_edges(), g.get_vertices(), sep='\n')
    #
    #
    # print("\nPDF - method is_valid_path() example 1")
    # print("--------------------------------------")
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # g = DirectedGraph(edges)
    # test_cases = [[0, 1, 4, 3], [1, 3, 2, 1], [0, 4], [4, 0], [], [2]]
    # print(g)
    # for path in test_cases:
    #     print(path, g.is_valid_path(path))
    #
    #
    # print("\nPDF - method dfs() and bfs() example 1")
    # print("--------------------------------------")
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # g = DirectedGraph(edges)
    # for start in range(5):
    #     print(f'{start} DFS:{g.dfs(start)} BFS:{g.bfs(start)}')
    #
    #
    # print("\nPDF - method has_cycle() example 1")
    # print("----------------------------------")
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # g = DirectedGraph(edges)
    # #
    # edges_to_remove = [(3, 1), (4, 0), (3, 2)]
    # for src, dst in edges_to_remove:
    #     g.remove_edge(src, dst)
    #     print(g.get_edges(), g.has_cycle(), sep='\n')
    # #
    # edges_to_add = [(4, 3), (2, 3), (1, 3), (4, 0)]
    # for src, dst in edges_to_add:
    #     g.add_edge(src, dst)
    #     print(g.get_edges(), g.has_cycle(), sep='\n')
    # print('\n', g)
    #
    #
    print("\nPDF - dijkstra() example 1")
    print("--------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    for i in range(5):
        print(f'DIJKSTRA {i} {g.dijkstra(i)}')
    g.remove_edge(4, 3)
    print('\n', g)
    for i in range(5):
        print(f'DIJKSTRA {i} {g.dijkstra(i)}')
