from typing import List
from collections import deque


# TLE : Code Time Complexity is O(N^2) (Sigma 1 to N)
# 30/47 tests passed.
class Solution1:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0 for i in range(len(temperatures))]
        day = 0
        for day in range(len(temperatures)):
            count = 1
            for futureDay in range(day + 1, len(temperatures)):
                if temperatures[futureDay] > temperatures[day]:
                    out[day] = count
                    break
                else:
                    count += 1

        return out


# Runtime: 1408 ms, faster than 61.16% of Python3 online submissions.
# Memory Usage: 24 MB, less than 97.08% of Python3 online submissions.
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        N = len(temperatures)
        out = [0 for i in range(N)]

        for i in range(N):
            val = temperatures[i]
            while stack:
                if stack[-1][0] < val:
                    popped = stack.pop()
                    out[popped[1]] = i - popped[1]
                else:
                    break
            stack.append((val, i))

        return out


sol = Solution()
print(sol.dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]))
