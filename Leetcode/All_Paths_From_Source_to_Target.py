from typing import List


class Solution:
    # Runtime: 227 ms, faster than 5.21% of Python3 online submissions.
    # Memory Usage: 15.8 MB, less than 23.66% of Python3 online submissions.
    # T : O(2^N), S : O(N)
    """
    I think the time complexity is O(2^n).
    Think about this worst case scenario:
    Suppose we have n nodes, labeled 0 to n-1.
    Think of it as an array: [0, 1, 2, 3, 4, 5, 6, ..., n-1]
    For each pair of nodes i and j, if i < j, let there be an edge between node i and node j.
    (So, there are O(n^2) edges, though this fact is not important.)
    Now, we want to calculate how many paths there are from the 0th node to the (n-1)th node.
    Well, notice that each path of length k corresponds to some choice of
    (k - 1) nodes between 0 and (n-1).
    For example, here are two paths of length 2:
    0->3->(n-1)
    0->5->(n-1)
    Here is a path of length 3:
    0->1->5->(n-1)
    How many paths of length k are there? The answer is (n-2 choose k-1) because we pick
    k - 1 nodes between 0 and (n - 1).
    The total number of paths is the sum of (n-2 choose k-1) for k = 1, 2, ..., (n-1).
    Using the binomial theorem, this sum is equal to 2^(n-2) which is O(2^n).
    """

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.start, self.end = 0, len(graph) - 1
        self.graph = graph
        self.paths = []
        self.traverse(0, [0])
        return self.paths

    def traverse(self, node, path):
        if node == self.end:
            self.paths.append(path[::])
            return
        # Not checking for loops, if any.
        if self.graph[node] == []:
            return
        for next_node in self.graph[node]:
            path.append(next_node)
            self.traverse(next_node, path)
            path.pop()

    # Runtime: 102 ms, faster than 88.68%.
    # Memory Usage: 15.6 MB, less than 78.57%.
    # T : O(Edges), S : O(Nodes)
    def allPathsSourceTarget1(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        src, dst = 0, len(graph) - 1

        def dfs(idx, path):
            if idx == dst:
                paths.append(path[:])
            for next in graph[idx]:
                path.append(next)
                dfs(next, path)
                path.pop()

        dfs(src, [src])
        return paths


if __name__ == "__main__":
    sol = Solution()
    assert (sol.allPathsSourceTarget(graph=[[4, 3, 1], [3, 2, 4], [3], [4], []])) == [
        [0, 4],
        [0, 3, 4],
        [0, 1, 3, 4],
        [0, 1, 2, 3, 4],
        [0, 1, 4],
    ]
    assert sol.allPathsSourceTarget(graph=[[1, 2], [3], [3], []]) == [[0, 1, 3], [0, 2, 3]]
