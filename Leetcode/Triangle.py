from typing import List


# Runtime: 85 ms, faster than 63.18% of Python3 online submissions for Triangle.
# Memory Usage: 15.2 MB, less than 33.19% of Python3 online submissions for Triangle.
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp: List[List[int]] = []
        for row_index in range(len(triangle)):
            row = triangle[row_index]
            if len(row) == 1:
                dp.append(row)
            else:
                dp.append([])
                prev_row = dp[row_index - 1]
                for i in range(len(row)):
                    curr_val = row[i]
                    prev_i = [i - 1, i]
                    allowed_prev_i = [_ for _ in prev_i if _ >= 0 and _ < len(prev_row)]
                    prev_val = min(prev_row[_] for _ in allowed_prev_i)
                    dp[row_index].append(prev_val + curr_val)

        return min(dp[-1])


# Runtime: 103 ms, faster than 41.21% of Python3 online submissions for Triangle.
# Memory Usage: 15 MB, less than 60.15% of Python3 online submissions for Triangle.
class SolutionSpaceOptimised:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp: List[int] = triangle[-1]

        for row_index in range(len(triangle) - 2, -1, -1):
            row = triangle[row_index]
            prev_row = dp
            for i in range(len(row)):
                curr_val = row[i]
                prev_i = [i + 1, i]
                allowed_prev_i = [_ for _ in prev_i if _ >= 0 and _ < len(prev_row)]
                prev_val = min(prev_row[_] for _ in allowed_prev_i)
                dp[i] = prev_val + curr_val

        return dp[0]


# sol = Solution()
# sol.minimumTotal(triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])


class Solution:
    # Runtime: 106 ms, faster than 54.11% of Python3 online submissions.
    # Memory Usage: 14.8 MB, less than 93.65% of Python3 online submissions.
    # T : O(N), S : O(N)
    # Where N is the number of rows in the triangle.
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = triangle[-1][::]
        for idx in range(n - 2, -1, -1):
            row = triangle[idx]
            for j in range(len(row)):
                dp[j] = min(dp[j], dp[j + 1]) + row[j]

        return dp[0]
