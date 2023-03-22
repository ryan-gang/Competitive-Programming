from collections import defaultdict, deque
from sys import maxsize
from StarterCode.Union_Find import Union


class Solution:
    # Runtime: 1948 ms, faster than 46.98%.
    # Memory Usage: 77.9 MB, less than 21.81%.
    # T : O(E), S : O(E) ; where E is the number of edges.
    # In the worst case we traverse each edge twice.
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        """
        As there is no restriction on path length. And 1 and n are guaranteed to
        be connected. We can just traverse all the edges, find the smallest
        distance edge, and return that. Because we can start from 1, travel to
        this edge, return to 1 and then go to n. So the problem basically is to
        find the smallest distance out of all the edges.
        """
        d: dict[int, list[list[int]]] = defaultdict(list)
        min_dist = maxsize
        for a, b, dist in roads:
            d[a].append([b, dist])
            d[b].append([a, dist])
            min_dist = min(min_dist, dist)

        queue = deque([1])
        seen: set[str] = set()
        min_dist_in_path = maxsize
        while queue:
            for _ in range(len(queue)):
                source = queue.popleft()
                for destination, dist in d[source]:
                    path = f"{source}:{destination}"
                    # if we put a node in the seen set, we might miss an edge.
                    # 1, 3, 4 are all connected. If we start from 1, we go to 3
                    # and 4 as they are at the same level. But then as 3 is
                    # already seen, we can't traverse the 4 -> 3 edge.
                    if path not in seen:
                        min_dist_in_path = min(min_dist_in_path, dist)
                        queue.append(destination)
                        seen.add(path)
            if min_dist_in_path == min_dist:
                break
        return min_dist_in_path

    # Runtime: 1879 ms, faster than 52.68%.
    # Memory Usage: 58.7 MB, less than 87.58%.
    # T : O(N), S : O(N) ; where N is number of nodes.
    def minScore1(self, n: int, roads: list[list[int]]) -> int:
        """
        Union all the edges.
        And then find the smallest distance from the nodes that are connected to 1.
        """
        answer = maxsize
        uf = Union(n + 1)
        for a, b, dist in roads:
            if not uf.exists(a):
                uf.new(a)
            if not uf.exists(b):
                uf.new(b)
            uf.union(a, b)

        for a, b, dist in roads:
            if uf.find(1) == uf.find(b) or uf.find(1) == uf.find(a):
                answer = min(answer, dist)
        return answer


if __name__ == "__main__":
    sol = Solution()
    assert sol.minScore1(n=4, roads=[[1, 2, 9], [2, 3, 1], [2, 4, 5], [1, 4, 7]]) == 1
    assert sol.minScore1(n=4, roads=[[1, 2, 2], [1, 3, 4], [3, 4, 7]]) == 2
