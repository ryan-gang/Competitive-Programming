from collections import deque
from typing import List
from StarterCode.decorators import timeit


class Solution:
    @timeit
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        return Solution.BFS2(maze, entrance)

    @staticmethod
    def BFS(maze, entrance):
        m, n = len(maze), len(maze[0])
        queue = deque()
        queue.append(entrance)
        steps = 0
        visited = set()

        while queue:
            for _ in range(len(queue)):
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                R, C = queue.popleft()
                if (R, C) in visited:
                    continue
                visited.add((R, C))
                if (R == 0 or C == 0 or R == m - 1 or C == n - 1) and ([R, C] != entrance):
                    return steps
                for x, y in directions:
                    r, c = R + x, C + y
                    if r >= 0 and c >= 0 and r < m and c < n and maze[r][c] == ".":
                        queue.append((r, c))
            steps += 1
        return -1

    @staticmethod
    # Runtime: 1995 ms, faster than 48.93%.
    # Memory Usage: 14.4 MB, less than 97.75%.
    # Uses less space, no visited set().
    def BFS2(maze, entrance):
        m, n = len(maze), len(maze[0])
        queue = deque()
        queue.append(entrance)
        steps = 0

        while queue:
            for _ in range(len(queue)):
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                R, C = queue.popleft()
                if maze[R][C] == "#":
                    continue
                maze[R][C] = "#"
                if (R == 0 or C == 0 or R == m - 1 or C == n - 1) and ([R, C] != entrance):
                    return steps
                for x, y in directions:
                    r, c = R + x, C + y
                    if r >= 0 and c >= 0 and r < m and c < n and maze[r][c] == ".":
                        queue.append((r, c))
            steps += 1
        return -1


if __name__ == "__main__":
    sol = Solution()
    assert (
        sol.nearestExit(
            maze=[["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]], entrance=[1, 2]
        ) == 1
    )
    assert (sol.nearestExit([["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], [1, 0])) == 2
    assert (sol.nearestExit([[".", "+"]], [0, 0])) == -1
    assert (
        sol.nearestExit(
            [
                ["+", ".", "+", "+", "+", "+", "+"],
                ["+", ".", "+", ".", ".", ".", "+"],
                ["+", ".", "+", ".", "+", ".", "+"],
                ["+", ".", ".", ".", ".", ".", "+"],
                ["+", "+", "+", "+", ".", "+", "."],
            ],
            [0, 1],
        )
    ) == 7
