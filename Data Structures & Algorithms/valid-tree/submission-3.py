class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # convert edges to graph
        graph = {}
        for src, dest in edges:
            if src in graph:
                graph[src] += [dest]
            else:
                graph[src] = [dest]
            if dest in graph:
                 graph[dest] += [src]
            else:
                graph[dest] = [src]

        if len(graph) == 0:
            return True

        # no cycle existed
        visited = set()
        queue = deque()
        queue.appendleft([-1,0])
        while queue:
            prev_node, current_node = queue.pop()
            if current_node in visited:
                return False
            visited.add(current_node)
            for next_node in graph[current_node]:
                if next_node != prev_node:
                    queue.appendleft([current_node, next_node])

        # connectivity
        return len(visited) == n 

        