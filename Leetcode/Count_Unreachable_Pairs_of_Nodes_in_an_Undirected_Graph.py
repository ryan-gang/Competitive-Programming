from collections import defaultdict
from StarterCode.Union_Find import Union
from collections import deque


class Solution:
    # Runtime: 2218 ms, faster than 55.87%.
    # Memory Usage: 101.8 MB, less than 36.30%.
    # T : O(N+E), S : O(N+E)
    def countPairs(self, n: int, edges: list[list[int]]) -> int:
        """
        Union all the connections, then find the root of each of the n nodes. We
        can get all the component roots, and their sizes from here.
        """
        uf = Union(n)
        for node in range(n):
            uf.new(node)

        for v1, v2 in edges:
            uf.union(v1, v2)

        roots: dict[int, int] = defaultdict(int)
        for node in range(n):
            root = uf.find(node)
            roots[root] += 1

        v = list(roots.values())  # All the component sizes.
        pairs = 0
        for node in v:  # For each component root
            pairs += node * (n - node)  # We multiply it with ALL the other nodes
        # And keep a track of this number.
        # We count each "pair" twice, so we divide by 2 finally.
        return pairs // 2

    # Runtime: 2168 ms, faster than 69.39%.
    # Memory Usage: 75.6 MB, less than 56.23%.
    # T : O(N+E), S : O(N+E)
    def countPairs1(self, n: int, edges: list[list[int]]) -> int:
        """
        For every node, we initiate a BFS from there, and see how many nodes we
        can reach. We keep a track of all these "components" and their sizes.
        """

        def bfs(src: int, graph: dict[int, list[int]], visited: set[int]) -> int:
            queue = deque([src])
            count = 0
            while queue:
                node = queue.popleft()
                if node in visited:
                    continue
                else:
                    count += 1
                    queue.extend(graph[node])
                visited.add(node)
            return count

        d: dict[int, list[int]] = defaultdict(list)
        for v1, v2 in edges:
            d[v1].append(v2)
            d[v2].append(v1)

        seen: set[int] = set()
        components: dict[int, int] = defaultdict(int)

        for node in range(n):
            if node not in seen:
                components[node] += bfs(node, d, seen)

        v = list(components.values())
        pairs = 0
        for node in v:
            pairs += node * (n - node)

        return pairs // 2


if __name__ == "__main__":
    sol = Solution()
    assert sol.countPairs(n=3, edges=[[0, 1], [0, 2], [1, 2]]) == 0
    assert sol.countPairs(n=7, edges=[[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]) == 14
