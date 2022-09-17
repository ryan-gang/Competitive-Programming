from typing import List

mat = [[0, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 0]]
# mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
# mat = [[0, 0, 0, 1, 1], [0, 0, 1, 1, 1], [0, 1, 1, 1, 1], [1, 1, 1, 1, 0]]
# mat = [
# [1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
# [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
# [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
# [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
# [0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
# [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
# [0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
# [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
# [1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
# [1, 1, 1, 1, 0, 1, 0, 0, 1, 1],
# ]


class Solution:
    # Runtime: 1598 ms, faster than 10.64% of Python3 online submissions.
    # Memory Usage: 17.2 MB, less than 58.29% of Python3 online submissions.
    # T : O(m*n), S : O(1) (Output array apparently doesn't count)
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        # Initialize dp array with all `None`s.
        dp = [[None for _ in range(n)] for __ in range(m)]

        # For all cells, if mat[i][j] is 0, fill it with 0,
        # else find the four neighbours, and fill it with min(neighbours) + 1
        for i in range(m):
            for j in range(n):
                possible_values = []
                if mat[i][j] == 0:
                    dp[i][j] = 0
                    continue
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        if k >= 0 and k < m and l >= 0 and l < n:
                            if abs((i + j) - (l + k)) == 1:
                                if dp[k][l] is not None:
                                    possible_values.append(dp[k][l])
                if not possible_values:
                    continue
                val = min(possible_values) + 1
                dp[i][j] = val
        # We run the dp logic, twice over the mat array,
        # Because if 0,0 has a 0, and 10, 10 has a 0.
        # 9,10 will be set as 17, but it should be 1.
        # The 0's later in the matrix, will not be taken into consideration.
        # So to let all the changes propagate, we run it twice.
        # Once from 0, 0 to 10, 10 again from 10, 10 to 0, 0
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                possible_values = []
                if mat[i][j] == 0:
                    dp[i][j] = 0
                    continue
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        if k >= 0 and k < m and l >= 0 and l < n:
                            if abs((i + j) - (l + k)) == 1:
                                if dp[k][l] is not None:
                                    possible_values.append(dp[k][l])
                if not possible_values:
                    continue
                val = min(possible_values) + 1
                dp[i][j] = val
        return dp

    # Without an extra dp array ? In place possible ? Not like this.
    # def updateMatrix2(self, mat: List[List[int]]) -> List[List[int]]:
    #     m, n = len(mat), len(mat[0])
    #     # Initialize dp array with all `None`s.

    #     # For all cells, if mat[i][j] is 0, fill it with 0,
    #     # else find the four neighbours, and fill it with min(neighbours) + 1
    #     for i in range(m):
    #         for j in range(n):
    #             possible_values = []
    #             if mat[i][j] == 0:
    #                 continue
    #             if mat[i][j] == 1:
    #                 mat[i][j] = float('inf')
    #             for k in range(i - 1, i + 2):
    #                 for l in range(j - 1, j + 2):
    #                     if k >= 0 and k < m and l >= 0 and l < n:
    #                         if abs((i + j) - (l + k)) == 1:
    #                             if mat[k][l] == 1:
    #                                 possible_values.append(float("inf"))
    #                             else:
    #                                 possible_values.append(mat[k][l])
    #             val = min(possible_values) + 1
    #             mat[i][j] = val
    #     # We run the dp logic, twice over the mat array,
    #     # Because if 0,0 has a 0, and 10, 10 has a 0.
    #     # 9,10 will be set as 17, but it should be 1.
    #     # The 0's later in the matrix, will not be taken into consideration.
    #     # So to let all the changes propagate, we run it twice.
    #     # Once from 0, 0 to 10, 10 again from 10, 10 to 0, 0
    #     # for i in range(m - 1, -1, -1):
    #     #     for j in range(n - 1, -1, -1):
    #     #         possible_values = []
    #     #         if mat[i][j] == 0:
    #     #             continue
    #     #         for k in range(i - 1, i + 2):
    #     #             for l in range(j - 1, j + 2):
    #     #                 if k >= 0 and k < m and l >= 0 and l < n:
    #     #                     if abs((i + j) - (l + k)) == 1:
    #     #                         possible_values.append(mat[k][l])
    #     #         val = min(possible_values) + 1
    #     #         mat[i][j] = val
    #     return mat


# To not use an extra array :
class Solution2:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] = float("inf") if matrix[i][j] == 1 else matrix[i][j]
                    if i > 0:
                        matrix[i][j] = min(matrix[i][j], matrix[i - 1][j] + 1)
                    if j > 0:
                        matrix[i][j] = min(matrix[i][j], matrix[i][j - 1] + 1)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if matrix[i][j] != 0:
                    if i < m - 1:
                        matrix[i][j] = min(matrix[i][j], matrix[i + 1][j] + 1)
                    if j < n - 1:
                        matrix[i][j] = min(matrix[i][j], matrix[i][j + 1] + 1)
        return matrix


sol = Solution()
print(sol.updateMatrix(mat))
