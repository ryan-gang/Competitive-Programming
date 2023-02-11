from collections import defaultdict, deque


class Solution:
    # Runtime: 85 ms, faster than 87.10%.
    # Memory Usage: 14.2 MB, less than 73.17%.
    # T : O(N), S : O(N)
    def shortestAlternatingPaths(
        self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]
    ) -> list[int]:
        """
        We can traverse all nodes in a graph using BFS, so when we visit a particular node
        we update the distance corresponding to that index in our output array. In our BFS
        queue, we keep a track of the node, and its corresponding previous color. Based on
        this color we choose the next node to travel to. There can be cases where we need
        to visit a specific node multiple times, from different coloured edges. For this we
        keep this (node, color) combination in our visited set.
        """
        red: dict[int, list[int]] = defaultdict(list)
        blue: dict[int, list[int]] = defaultdict(list)
        out = [-1] * n

        for start, end in redEdges:
            red[start].append(end)

        for start, end in blueEdges:
            blue[start].append(end)

        dist = 0
        START = [(0, "r"), (0, "b")]
        queue: deque[tuple[int, str]] = deque(START)
        visited: set[tuple[int, str]] = set(START)
        while queue:
            for _ in range(len(queue)):
                node, prev_color = queue.popleft()
                if out[node] == -1:
                    out[node] = dist
                if prev_color == "r":
                    for nxt in blue[node]:
                        if (nxt, "b") not in visited:
                            queue.append((nxt, "b"))
                            visited.add((nxt, "b"))
                if prev_color == "b":
                    for nxt in red[node]:
                        if (nxt, "r") not in visited:
                            queue.append((nxt, "r"))
                            visited.add((nxt, "r"))

            dist += 1

        return out


if __name__ == "__main__":
    sol = Solution()
    assert (sol.shortestAlternatingPaths(n=3, redEdges=[[0, 1], [1, 2]], blueEdges=[])) == [
        0,
        1,
        -1,
    ]
    assert (sol.shortestAlternatingPaths(n=3, redEdges=[[0, 1]], blueEdges=[[2, 1]])) == [0, 1, -1]
    assert (sol.shortestAlternatingPaths(n=3, redEdges=[[0, 1], [0, 2]], blueEdges=[[1, 0]])) == [
        0,
        1,
        1,
    ]
    assert (
        sol.shortestAlternatingPaths(
            n=5, redEdges=[[0, 1], [1, 2], [2, 3], [3, 4]], blueEdges=[[1, 2], [2, 3], [3, 1]]
        )
    ) == [0, 1, 2, 3, 7]
