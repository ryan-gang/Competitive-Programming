from typing import List


# Runtime: 69 ms, faster than 95.75% of Python3 online submissions for Transpose Matrix.
# Memory Usage: 14.7 MB, less than 55.33% of Python3 online submissions for Transpose Matrix.
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        out = [[None for __ in range(m)] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if not out[j][i]:
                    out[j][i] = matrix[i][j]

        return out


class Solution1L:
    # https://stackoverflow.com/questions/5239856/
    def transpose(self, A):
        return list(zip(*A))
