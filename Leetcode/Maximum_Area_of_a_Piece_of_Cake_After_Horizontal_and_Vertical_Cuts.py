from typing import List


h = 5
w = 4
horizontalCuts = [4, 2, 1]
verticalCuts = [1, 3]
# horizontalCuts and verticalCuts can be unsorted, we will sort it first.
# The order will be required in our code.
# Instead of storing it in a variable, we will sort it and pass to our helper method.
# The helper method, calculates the width of each "division" after making the cuts.
# Then we take the 2 largest divisions, and find the cell with those 2 as row and col.


class Solution:
    # Runtime: 316 ms, faster than 98.45% of Python3 online submissions...
    # Memory Usage: 31.4 MB, less than 8.75% of Python3 online submissions...
    # No noticable performance gain by using inPlace helper.
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalDivs = self.getDivisionsInplace(sorted(horizontalCuts), h)
        verticalDivs = self.getDivisionsInplace(sorted(verticalCuts), w)

        out = max(horizontalDivs) * max(verticalDivs)
        modulo = pow(10, 9) + 7
        return out % modulo

    # So instead of using this helper, and appending all values to a list,
    # just keep the max value at every iteration.
    # That is what we require, right.
    def getDivisions(self, cuts: List[int], length: int) -> List[int]:
        divs, start = [], 0
        for i in cuts:
            val = i - start
            start = i
            divs.append(val)
        divs.append(length - i)
        return divs

    def getDivisionsInplace(self, cuts: List[int], length: int) -> List[int]:
        start = 0
        for i, v in enumerate(cuts):
            val = v - start
            start = v
            cuts[i] = val
        cuts.append(length - v)
        return cuts


sol = Solution()
print(sol.maxArea(5, 4, [1, 2, 4], [1, 3]))

# Optimising step, I am failing.
# Don't store values to be computed on later, compute right then, and discard.