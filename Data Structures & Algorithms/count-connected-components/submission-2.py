class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if len(edges) == 0:
            return n
        d = {}
        for src, dest in edges:
            if src in d:
                d[src].append(dest)
            else:
                d[src] = [dest]
            if dest in d:
                d[dest].append(src)
            else:
                d[dest] = [src]

        def visit(n, visited):
            print(d)
            if n in visited:
                return 0
            if n not in d:
                return 1
            q = [n]
            while q:
                current = q.pop(0)
                if current in visited:
                    continue
                visited.add(current)
                for adj in d[current]:
                    if adj not in visited:
                        q.append(adj)
            return 1
            

        count = 0
        visited = set()
        for i in range(0, n):
            print(list(visited))
            count += visit(i, visited)

        return count 














        