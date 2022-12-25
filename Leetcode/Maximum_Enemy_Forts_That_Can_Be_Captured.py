from typing import List


class Solution:
    def captureFortsSelf(self, forts: List[int]) -> int:
        """
        Takes 1 forward, and 1 backward pass over the array, counting the number of 0's
        between 1's and -1's.
        """
        n = len(forts)
        max_captured = 0
        captured = 0
        flag = False
        for i in range(n):
            if forts[i] == 1:
                captured = 0
                flag = True
                continue
            elif forts[i] == -1:
                flag = False
                max_captured = max(captured, max_captured)
                captured = 0
            if flag:
                captured += 1

        flag = False
        captured = 0
        for i in range(n - 1, -1, -1):
            if forts[i] == 1:
                captured = 0
                flag = True
                continue
            elif forts[i] == -1:
                flag = False
                max_captured = max(captured, max_captured)
                captured = 0
            if flag:
                captured += 1

        return max_captured if max_captured > 0 else 0

    def captureForts(self, forts: List[int]) -> int:
        """
        Much much cleaner code.
        """
        ans = ii = 0
        for i, x in enumerate(forts):
            if x:
                if forts[ii] == -x:
                    ans = max(ans, i - ii - 1)
                ii = i
        return ans
