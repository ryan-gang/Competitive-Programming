# Wrong solution.
# class Solution:
#     def dfs(self, i, j):
#         if i <= 0 or i >= self.m or j <= 0 or j >= self.n:
#             return 0
#         surrounding = 0
#         out = 0
#         for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#             ii, jj = i + di, j + dj
#             if ii <= 0 and ii >= self.m and j <= 0 and j >= self.n:
#                 if board[ii][jj] == "X":
#                     surrounding += 1

#             if surrounding == 3:
#                 print("Yes !", i, j)
#                 board[i][j] = "O"
#                 return 3

#         for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#             ii, jj = i + di, j + dj
#             if board[ii][jj] == "O":
#                 out = max(out, self.dfs(ii, jj))

#             if out == 3:
#                 board[i][j] = "O"
#                 return 3

#         return max(surrounding, out)

#     def solve(self, board):
#         self.m, self.n = len(board), len(board[0])
#         for x, row in enumerate(board):
#             for y, cell in enumerate(row):
#                 if cell == "O":
#                     self.dfs(x, y)


import collections


# Ref : https://leetcode.com/problems/surrounded-regions/discuss/41652/
# Python-easy-to-understand-DFS-and-BFS-solutions
class Solution:
    # Runtime: 273 ms, faster than 27.54% of Python3 online submissions.
    # Memory Usage: 16 MB, less than 39.42% of Python3 online submissions.
    def solve(self, board):
        self.m, self.n = len(board), len(board[0])
        self.board = board
        # Run dfs for all cells in first and last row.
        # So that all connected 0's are now "#"
        # These 0's are connected to 0's at the edge, they should not be "captured".
        for i in [0, self.m - 1]:
            for j in range(self.n):
                self.dfs(i, j)
        # Run dfs for all cells in first and last column.
        for i in range(self.m):
            for j in [0, self.n - 1]:
                self.dfs(i, j)

        # At this point, all the "forbidden" 0's are marked with "#",
        # now proceed to capture the rest.
        # They are not connected to "forbidden" 0's and even if
        # they are connected to other 0's or they are solo, all these are fair game.
        for i in range(self.m):
            for j in range(self.n):
                if self.board[i][j] == "#":
                    self.board[i][j] = "O"
                elif self.board[i][j] == "O":
                    self.board[i][j] = "X"

    # If surrounding cells are connected to a 0, convert all to the same char.
    def dfs(self, i, j):
        if i >= 0 and i < self.m and j >= 0 and j < self.n and self.board[i][j] == "O":
            self.board[i][j] = "#"
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ii, jj = i + di, j + dj
                self.dfs(ii, jj)

    # BFS
    def solveBFS(self, board):
        queue = collections.deque([])
        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r in [0, len(board) - 1] or c in [0, len(board[0]) - 1]) and board[r][c] == "O":
                    queue.append((r, c))
        while queue:
            r, c = queue.popleft()
            if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == "O":
                board[r][c] = "."
                queue.extend([(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)])

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == ".":
                    board[r][c] = "O"


board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "O", "O", "X"], ["X", "O", "X", "X"]]
print("prev")
for i in board:
    print(i)
sol = Solution()
sol.solve(board)
print("after")
for i in sol.board:
    print(i)
