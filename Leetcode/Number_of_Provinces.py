from Leetcode.StarterCode.disjoint_set_union import Union


class Solution:
    """
    Use a disjoint set union data structure to efficiently perform union
    operations, and finally get the count of parent nodes.
    """

    # T : O(N^2), S : O(N)
    def findCircleNum(self, is_connected: list[list[int]]) -> int:
        n = len(is_connected)
        uf = Union(n)
        for i in range(n):
            if not uf.exists(i):
                uf.new(i)

        for r, row in enumerate(is_connected):
            for c, cell in enumerate(row):
                if cell:
                    uf.union(r, c)

        return uf.count_parents()


class Solution1:
    # Runtime: 467 ms, faster than 8.48% of Python3 online submissions.
    # Memory Usage: 14.2 MB, less than 96.29% of Python3 online submissions.
    # T : O(N * N), S : O(N)
    # Proper DFS solution. For each node check if each of its neighbours are visited or not,
    # if not visited, visit them now. And add all them to a visited set.
    # After current iteration, increment counter.
    # All provinces connected to this node, are already counted into this 1.
    def dfs(self, node: int):
        for nei, adj in enumerate(self.is_connected[node]):
            if adj and nei not in self.seen:
                self.seen.add(nei)
                self.dfs(nei)

    def findCircleNum(self, is_connected: list[list[int]]) -> int:
        self.seen: set[int] = set()
        self.is_connected = is_connected
        n, provinces = len(is_connected), 0

        for node in range(n):
            if node not in self.seen:
                self.dfs(node)
                provinces += 1

        return provinces

    # For every iteration, take a node, initially if this is not seen, add it onto a queue
    # While these queue is not empty go on visiting nodes, and after each visited node, add
    # it's neighbours onto the queue, so they will also be visited in this province itself.
    def findCircleNumBFS(self, is_connected: list[list[int]]) -> int:
        seen = set([])
        res = 0
        for i in range(len(is_connected)):
            if i not in seen:
                to_see: list[int] = [i]
                while len(to_see):
                    cur = to_see.pop()
                    if cur not in seen:
                        seen.add(cur)
                        to_see = [
                            j for j, v in enumerate(is_connected[cur]) if v and j not in seen
                        ] + to_see
                res += 1
        return res


if __name__ == "__main__":
    sol = Solution()
    assert sol.findCircleNum(is_connected=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
    assert sol.findCircleNum(is_connected=[[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3
    assert (
        sol.findCircleNum(is_connected=[[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]])
        == 1
    )
