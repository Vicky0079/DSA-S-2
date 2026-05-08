from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))

    def bfs(self, start):
        visited = set()
        queue = deque([start])

        visited.add(start)

        print("BFS Traversal:")

        while queue:
            node = queue.popleft()
            print(node, end=" ")

            for neighbor, weight in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        print()

    def dfs_util(self, node, visited):
        visited.add(node)

        print(node, end=" ")

        for neighbor, weight in self.graph[node]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self, start):
        visited = set()

        print("DFS Traversal:")

        self.dfs_util(start, visited)

        print()