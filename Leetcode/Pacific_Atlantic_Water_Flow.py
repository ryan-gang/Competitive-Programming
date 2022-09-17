from typing import List


# 50/113 TC passed. Wrong answer.
# DFS has to propagate to all neighbouring nodes, not just selective left and top nodes.
# But that is giving recursion error, nodes calling each other.
class SolutionWrong:
    def seekPacific(self, i, j):
        if i == 0 or j == 0:
            return True
        out = False
        current = self.heights[i][j]
        # Only go left and up.
        for di, dj in [(0, -1), (-1, 0)]:
            ii, jj = i + di, j + dj
            if self.heights[ii][jj] <= current:
                out = max(out, self.seekPacific(ii, jj))

        return out

    def seekAtlantic(self, i, j):
        if i == (self.m - 1) or j == (self.n - 1):
            return True
        out = False
        current = self.heights[i][j]
        # Only go right and down.
        for di, dj in [(0, 1), (1, 0)]:
            ii, jj = i + di, j + dj
            if self.heights[ii][jj] <= current:
                out = max(out, self.seekAtlantic(ii, jj))

        return out

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.heights = heights
        self.m, self.n = len(heights), len(heights[0])
        out = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                flag1 = self.seekPacific(i, j)
                flag2 = self.seekAtlantic(i, j)
                flag = flag1 and flag2
                if flag:
                    out.append((i, j))

        return out


# 28 / 113 TC passed. TLE.
class SolutionTLE:
    def seekPacific(self, i, j, visited):
        visited[i][j] = 1
        if i == 0 or j == 0:
            return True
        out = False
        current = self.heights[i][j]
        for di, dj in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            ii, jj = i + di, j + dj
            if ii < 0 or ii >= self.m or jj < 0 or jj >= self.n or visited[ii][jj]:
                continue
            if self.heights[ii][jj] <= current:
                out = max(out, self.seekPacific(ii, jj, visited))

        return out

    def seekAtlantic(self, i, j, visited):
        visited[i][j] = 1
        if i == (self.m - 1) or j == (self.n - 1):
            return True
        out = False
        current = self.heights[i][j]
        for di, dj in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            ii, jj = i + di, j + dj
            if ii < 0 or ii >= self.m or jj < 0 or jj >= self.n or visited[ii][jj]:
                continue
            if self.heights[ii][jj] <= current:
                out = max(out, self.seekAtlantic(ii, jj, visited))

        return out

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.heights = heights
        self.m, self.n = len(heights), len(heights[0])
        out = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                visited = [[0 for _ in range(self.n)] for __ in range(self.m)]
                flag1 = self.seekPacific(i, j, visited)
                # if flag1:
                #     print("Pacific", (i, j))
                if flag1:
                    visited = [[0 for _ in range(self.n)] for __ in range(self.m)]
                    flag2 = self.seekAtlantic(i, j, visited)
                    # if flag2:
                    #     print("Atlantic", (i, j))
                    if flag2:
                        out.append((i, j))

        return out


# 3445 ms, faster than 5.35% of Python3 online submissions.
# Memory Usage: 15.6 MB, less than 78.42% of Python3 online submissions.
# Adding the `if out : return out` line to dfs, cuts runtime by 66%. Old runtime 9841ms.
# T : O(MxNx((MxN) + (MxN)), S : O(MxN)
# For all the cells in the matrix, we are running dfs on them.
# Worst case we will visit each cell again. Twice, for Atlantic dfs and Pacific dfs.
class Solution:
    def seekPacific(self, i, j, visited):
        # Add current i, j to a set, so as to not come back to this index in the
        # next iterations of this dfs call itself.
        visited.add((i, j))
        if i == 0 or j == 0:
            # We have reached the Pacific. Return True,
            # to signify Pacific can be reached from the calling index.
            return True
        out = False
        current = self.heights[i][j]
        # Need to traverse all neighbours.
        for di, dj in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            ii, jj = i + di, j + dj
            # If new indices out of range, or if we have already visited it
            # in this call stack itself, don't propagate there.
            if ii < 0 or ii >= self.m or jj < 0 or jj >= self.n or (ii, jj) in visited:
                continue
            if self.heights[ii][jj] <= current:
                # Out will store if we can reach Pacific anyway through all the dfs calls.
                out = max(out, self.seekPacific(ii, jj, visited))
                if out:
                    return out
        # Return out, default was False.
        return out

    def seekAtlantic(self, i, j, visited):
        visited.add((i, j))
        if i == (self.m - 1) or j == (self.n - 1):
            return True
        out = False
        current = self.heights[i][j]
        for di, dj in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            ii, jj = i + di, j + dj
            if ii < 0 or ii >= self.m or jj < 0 or jj >= self.n or (ii, jj) in visited:
                continue
            if self.heights[ii][jj] <= current:
                out = max(out, self.seekAtlantic(ii, jj, visited))
                if out:
                    return out
        return out

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.heights = heights
        self.m, self.n = len(heights), len(heights[0])
        out = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                # For all the indices, start dfs here, to check if we can reach Pacific.
                pacific_within_reach = self.seekPacific(i, j, visited=set())
                if pacific_within_reach:
                    # If pacific can be reached, only then try to check Atlantic reach.
                    atlantic_within_reach = self.seekAtlantic(i, j, visited=set())
                    if atlantic_within_reach:
                        # If both oceans are within reach, add index to output.
                        out.append((i, j))

        return out


sol = Solution()
print(sol.pacificAtlantic(heights=[[1, 2, 3], [8, 9, 4], [7, 6, 5]]))
