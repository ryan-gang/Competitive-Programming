# from collections import defaultdict
from typing import List

# Incorrect answer.
# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         n, partitions = len(isConnected), 0
#         self.d = defaultdict(list)
#         self.d_partitions = {}
#         self.seen = set()
#         for row, row_data in enumerate(isConnected):
#             for col, cell in enumerate(row_data):
#                 if row < col:
#                     row_idx, col_idx = row + 1, col + 1
#                     if cell == 1:
#                         self.d[row_idx].append(col_idx)

#         def recurse(connected_islands, partitions):
#             for i in connected_islands:
#                 self.seen.add(i)
#                 self.d_partitions[i] = partitions
#                 if i in self.d:
#                     recurse(self.d[i], partitions)

#         for i in range(1, n + 1):
#             if i not in self.seen:
#                 partitions += 1
#                 recurse([i], partitions)

#         return partitions


class Solution:
    # Runtime: 467 ms, faster than 8.48% of Python3 online submissions.
    # Memory Usage: 14.2 MB, less than 96.29% of Python3 online submissions.
    # T : O(N * N), S : O(N)
    # Proper DFS solution. For each node check if each of its neighbours are visited or not,
    # if not visited, visit them now. And add all them to a visited set.
    # After current iteration, increment counter.
    # All provinces connected to this node, are already counted into this 1.
    def dfs(self, node):
        for nei, adj in enumerate(self.isConnected[node]):
            if adj and nei not in self.seen:
                self.seen.add(nei)
                self.dfs(nei)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.seen = set()
        self.isConnected = isConnected
        n, provinces = len(isConnected), 0

        for node in range(n):
            if node not in self.seen:
                self.dfs(node)
                provinces += 1

        return provinces

    # For every iteration, take a node, initially if this is not seen, add it onto a queue
    # While these queue is not empty go on visiting nodes, and after each visited node, add
    # it's neighbours onto the queue, so they will also be visited in this province itself.
    def findCircleNumBFS(self, M):
        seen = set([])
        res = 0
        for i in range(len(M)):
            if i not in seen:
                toSee = [i]
                while len(toSee):
                    cur = toSee.pop()
                    if cur not in seen:
                        seen.add(cur)
                        toSee = [j for j, v in enumerate(M[cur]) if v and j not in seen] + toSee
                res += 1
        return res


sol = Solution()
print(
    sol.findCircleNum(
        isConnected=[
            [1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 1],
            [1, 1, 1, 0, 0, 0, 1],
            [0, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 1, 1, 0, 0, 0, 1],
        ]
    )
)
assert sol.findCircleNum(isConnected=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
assert sol.findCircleNum(isConnected=[[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3
assert sol.findCircleNum([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]) == 1
