"""1. Brute Force.
For every element in the array, we can find how much water that element can
hold, by calculating the min of the 2 boundaries (max heights) surrounding this element.

2. Optimizing Brute force, using a dp array.
Instead of calculating the max_left and max_right at
every iteration. Calculate them once, and store in an array.

3. Monotonic stack.
Both of these were unoptimised solutions, using multiple iterations of the
height array. We can write an algo using only 1 pass of the array. We use a monotonic stack,
to keep track of the decreasing heights, when we get a height higher than the previous one,
we pop the last (lower height) and calculate the area bounded by the (lower height's left height)
and this height. And keep on doing this while the current height is larger than any of the ones
pushed to the stack. When the stack is again monotonic decreasing we push the current element.

4. Two Pointer. From the 2nd approach, instead of precomputing the max_left and max_right values,
we can compute them JIT (just in time). We need only max_left, max_right and current height to
find the possible water trapped in current height.
We start with maxLeft = height[0], maxRight = height[n-1],
using 2 pointers left point to the next bar on the left side, right point to the
next bar on the right side.
How to decide to move left or move right?
If maxLeft < maxRight, it means the water level is based on the left side (the left bar is smaller)
then move left side:
If height[left] > maxLeft then there is no trap water, we update maxLeft by maxLeft = height[left].
Else if height[left] < maxLeft then it can trap an amount of water, which is maxLeft - height[left]
Move left by left += 1 Else if maxLeft > maxRight, it means the water level is based on the right
side (the right bar is smaller) then move right side: If height[right] > maxRight then there is no
trap water, we update maxRight by maxRight = height[right]. Else if height[right] < maxRight
then it can trap an amount of water, which is maxRight - height[right].
Move right by right -= 1. """


from collections import deque
from typing import List


class Solution:
    def trapBF(self, height: List[int]) -> int:
        water = 0
        n = len(height)
        for i, v in enumerate(height):
            max_left, max_right = 0, 0
            for _ in range(0, i):
                max_left = max(height[_], max_left)
            for _ in range(i, n):
                max_right = max(height[_], max_right)
            max_possible_height = min(max_left, max_right)
            water_height = max_possible_height - v

            if water_height > 0:
                water += water_height * 1

        return water

    # Runtime: 282 ms, faster than 20.74% of Python3 online submissions.
    # Memory Usage: 15.9 MB, less than 81.24% of Python3 online submissions.
    def trapDP1(self, height: List[int]) -> int:
        water = 0
        n = len(height)
        left = [0 for _ in range(n)]
        right = [0 for _ in range(n)]
        left[0] = height[0]
        right[n - 1] = height[n - 1]
        for i in range(n):
            left[i] = max(left[i - 1], height[i])
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], height[i])

        for i, v in enumerate(height):
            max_left, max_right = left[i], right[i]
            max_possible_height = min(max_left, max_right)
            water_height = max_possible_height - v

            if water_height > 0:
                water += water_height * 1

        return water

    # Ref : https://leetcode.com/problems/trapping-rain-water/
    # discuss/178028/Stack-with-Explanation-(Java-Python-Scala)
    # Runtime: 129 ms, faster than 94.23% of Python3 online submissions.
    # Memory Usage: 16.1 MB, less than 44.51% of Python3 online submissions.
    def trapMonotonicStack(self, height: List[int]) -> int:
        stack = deque()
        n = len(height)
        current = 0
        water = 0
        while current < n:
            while stack and height[current] > height[stack[-1]]:
                lower_height = height[stack.pop()]
                # We still need a left boundary of some sort, else water can't be trapped.
                if not stack:
                    break
                left_boundary = height[stack[-1]]
                right_boundary = height[current]
                max_possible_height = min(left_boundary, right_boundary)
                water_height = max_possible_height - lower_height
                water_width = current - stack[-1] - 1

                water += water_width * water_height
            stack.append(current)
            current += 1

        return water

    # Runtime: 251 ms, faster than 32.29% of Python3 online submissions.
    # Memory Usage: 16 MB, less than 81.24% of Python3 online submissions.
    def trapTwoPointer(self, height: List[int]) -> int:
        n = len(height)
        water = 0
        left, right = 0, n - 1
        max_left = max_right = 0
        while left < right:
            if height[left] < height[right]:
                # Water height is dependent on height[left], so we will increment this.
                if height[left] > max_left:
                    max_left = height[left]
                else:
                    water_height = max_left - height[left]
                    water += water_height
                left += 1
            else:
                if height[right] > max_right:
                    max_right = height[right]
                else:
                    water_height = max_right - height[right]
                    water += water_height
                right -= 1

        return water


sol = Solution()
assert (sol.trapDP1(height=[4, 2, 0, 3, 2, 5])) == 9
assert sol.trapDP1(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
