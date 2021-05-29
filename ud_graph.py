# Course: 
# Author: 
# Assignment: 
# Description:


class UndirectedGraph:
    """
    Class to implement undirected graph
    - duplicate edges not allowed
    - loops not allowed
    - no edge weights
    - vertex names are strings
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.adj_list = dict()

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            for u, v in start_edges:
                self.add_edge(u, v)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = [f'{v}: {self.adj_list[v]}' for v in self.adj_list]
        out = '\n  '.join(out)
        if len(out) < 70:
            out = out.replace('\n  ', ', ')
            return f'GRAPH: {{{out}}}'
        return f'GRAPH: {{\n  {out}}}'

    # ------------------------------------------------------------------ #

    def add_vertex(self, v: str) -> None:
        """
        Add new vertex to the graph. If the vertex is already present
        do nothing.
        """
        # Adds a new key with an empty list to the graph
        self.adj_list[v] = []

    def add_edge(self, u: str, v: str) -> None:
        """
        Add edge to the graph
        """

        # same vertex
        if u == v:
            return

        # Check if either vertex is not in the graph
        if u not in self.adj_list.keys():
            self.adj_list[u] = []

        if v not in self.adj_list.keys():
            self.adj_list[v] = []

        # add u to v's list and v to u's list
        u_list = self.adj_list[v]
        if u not in self.adj_list[v]:
            self.adj_list[v].append(u)

        if v not in self.adj_list[u]:
            self.adj_list[u].append(v)


    def remove_edge(self, v: str, u: str) -> None:
        """
        Remove edge from the graph
        """
        # Vertex not in graph
        if v not in self.adj_list.keys():
            return
        if u not in self.adj_list.keys():
            return

        # remove u from v
        v_list = self.adj_list[v]
        v_list.remove(u)

        # remove v from u
        u_list = self.adj_list[u]
        u_list.remove(v)


    def remove_vertex(self, v: str) -> None:
        """
        Remove vertex and all connected edges
        """

        if v not in self.adj_list.keys():
            return

        # remove v from all edges
        v_neighbors = self.adj_list[v]
        for value in v_neighbors:
            neighbor_list = self.adj_list[value]
            neighbor_list.remove(v)

        # remove v from the graph
        self.adj_list.pop(v)


    def get_vertices(self) -> []:
        """
        Return list of vertices in the graph (any order)
        """
        vertices = []
        for value in self.adj_list:
            vertices.append(value)

        return vertices


    def get_edges(self) -> []:
        """
        Return list of edges in the graph (any order)
        """
        edges = []

        # all vertices in graph
        vertices = self.get_vertices()

        # check each vertices edges
        for value in vertices:
            v_edges = self.adj_list[value]
            # get each neighboring vertex
            for u in v_edges:
                # check if v, u or u,v is already in edges
                if (value, u) in edges or (u, value) in edges:
                    continue
                else:
                    edges.append((value, u))

        return edges


    def is_valid_path(self, path: []) -> bool:
        """
        Return true if provided path is valid, False otherwise
        """
        counter = 0

        if len(path) == 0:
            return True

        if len(path) == 1:
            if path[0] not in self.adj_list.keys():
                return False

        for i in range(len(path) - 1):
            current_vertex = path[i]

            next_vertex = path[i + 1]
            if next_vertex in self.adj_list[current_vertex]:
                continue
            else:
                return False
        return True

        # visited = []
        # test = self.is_valid_path_recusive(path, 0, 0, visited)
        # return test

    # def is_valid_path_recusive(self, path: [], index, counter, visited):
    #     """
    #     Helper method to recursively follow a path
    #     """
    #
    #     if counter == len(path) - 1:
    #         return True
    #
    #     if len(path) == 0:
    #         return True
    #
    #     current_vertex = path[index]
    #     next_vertex = path[index + 1]
    #
    #     if next_vertex in self.adj_list[current_vertex]:
    #         visited.append(current_vertex)
    #         if self.is_valid_path_recusive(path, index + 1, counter + 1, visited):
    #             return True
    #         else:
    #             return False

    def dfs(self, v_start, v_end=None) -> []:
        """
        Return list of vertices visited during DFS search
        Vertices are picked in alphabetical order
        """

        # 1) initialize hash table of vertices
        visited = {}
        keys = self.adj_list.keys()
        for key in keys:
            visited[key] = False
        #
        # e.g {'A': true, 'B': false...}
        # 2) initialize empty stack
        # append() to add to top, pop() to remove from top

        stack = []
        traveled_vertex_list = []
        stack.append(v_start)


        # repeat until stack is not empty
        while len(stack) != 0:
            top = stack.pop()

            # end point
            # TODO: figure out how to append stop position if found

            # check if v_end is in vertex's neighbors
            # append current vertex and end vertex
            # to the traveled list and break the loop

            if top == v_end:
                traveled_vertex_list.append(top)
                break


            elif top != v_end and not visited[top]:
                # # put next traveled into
                traveled_vertex_list.append(top)
                # set top of stack as visited
                visited[top] = True
                # add each successor of vertex to the stack
                successors = self.adj_list[top]
                successors.sort(reverse=True)

                for vertex in successors:
                    stack.append(vertex)

        return traveled_vertex_list



    def bfs(self, v_start, v_end=None) -> []:
        """
        Return list of vertices visited during BFS search
        Vertices are picked in alphabetical order
        """

        # 1) initialize hash table of vertices
        visited = {}
        keys = self.adj_list.keys()
        for key in keys:
            visited[key] = False
        #
        # e.g {'A': true, 'B': false...}
        # 2) initialize empty stack
        # append() to add to top, pop() to remove from top

        stack = []
        traveled_vertex_list = []
        stack.append(v_start)




    def count_connected_components(self):
        """
        Return number of connected componets in the graph
        """


    def has_cycle(self):
        """
        Return True if graph contains a cycle, False otherwise
        """


if __name__ == '__main__':

    print("\nPDF - method add_vertex() / add_edge example 1")
    print("----------------------------------------------")
    g = UndirectedGraph()
    print(g)

    for v in 'ABCDE':
        g.add_vertex(v)
    print(g)

    g.add_vertex('A')
    print(g)

    for u, v in ['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE', ('B', 'C')]:
        g.add_edge(u, v)
    print(g)

    print("\nPDF - method remove_edge() / remove_vertex example 1")
    print("----------------------------------------------------")
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    g.remove_vertex('DOES NOT EXIST')
    g.remove_edge('A', 'B')
    g.remove_edge('X', 'B')
    print(g)
    g.remove_vertex('D')
    print(g)

    print("\nPDF - method get_vertices() / get_edges() example 1")
    print("---------------------------------------------------")
    g = UndirectedGraph()
    print(g.get_edges(), g.get_vertices(), sep='\n')
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE'])
    print(g.get_edges(), g.get_vertices(), sep='\n')

    print("\nPDF - method is_valid_path() example 1")
    print("--------------------------------------")
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    test_cases = ['ABC', 'ADE', 'ECABDCBE', 'ACDECB', '', 'D', 'Z']
    # test_cases = ['Z']
    for path in test_cases:
        print(list(path), g.is_valid_path(list(path)))

    #
    print("\nPDF - method dfs() and bfs() example 1")
    print("--------------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = 'ABCDEGH'
    for case in test_cases:
        print(f'{case} DFS:{g.dfs(case)} BFS:{g.bfs(case)}')
    print('-----')
    for i in range(1, len(test_cases)):
        v1, v2 = test_cases[i], test_cases[-1 - i]
        print(f'{v1}-{v2} DFS:{g.dfs(v1, v2)} BFS:{g.bfs(v1, v2)}')


    # print(f'DFS C-E: {g.dfs("C", "E")}')
    #
    #
    # print("\nPDF - method count_connected_components() example 1")
    # print("---------------------------------------------------")
    # edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    # g = UndirectedGraph(edges)
    # test_cases = (
    #     'add QH', 'remove FG', 'remove GQ', 'remove HQ',
    #     'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
    #     'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
    #     'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG')
    # for case in test_cases:
    #     command, edge = case.split()
    #     u, v = edge
    #     g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
    #     print(g.count_connected_components(), end=' ')
    # print()
    #
    #
    # print("\nPDF - method has_cycle() example 1")
    # print("----------------------------------")
    # edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    # g = UndirectedGraph(edges)
    # test_cases = (
    #     'add QH', 'remove FG', 'remove GQ', 'remove HQ',
    #     'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
    #     'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
    #     'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG',
    #     'add FG', 'remove GE')
    # for case in test_cases:
    #     command, edge = case.split()
    #     u, v = edge
    #     g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
    #     print('{:<10}'.format(case), g.has_cycle())
