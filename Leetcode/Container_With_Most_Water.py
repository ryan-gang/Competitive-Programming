from typing import List


class Solution:
    # Runtime: 1473 ms, faster than 11.77%.
    # Memory Usage: 27.4 MB, less than 54.42%.
    def maxArea(self, height: List[int]) -> int:
        lo, hi = 0, len(height) - 1
        maxArea = area = 0
        while lo < hi:
            area = (hi - lo) * min(height[lo], height[hi])
            maxArea = max(maxArea, area)
            if height[lo] < height[hi]:
                # height[lo] can't be used to achieve a higher vol of water
                # So we can try to use the next container, and a lower width
                lo += 1
            elif height[lo] > height[hi]:
                hi -= 1
            else:
                lo += 1
                hi -= 1

        return maxArea

    # Runtime: 1423 ms, faster than 17.48%.
    # Memory Usage: 26.1 MB, less than 99.09%.
    # T : O(N), S : O(1)
    def maxArea2(self, height: List[int]) -> int:
        start, end = 0, len(height) - 1
        max_area = 0
        while start <= end:
            area = (end - start) * min(height[start], height[end])
            max_area = max(area, max_area)
            # The smaller stick, is not doing anything here,
            # the container vol is actually "constrained" by this.
            # So the only way to change it, is by changing the smaller stick.
            # The longer stick is not being used to calculate the area anyway.
            # The only problem may hypothetically arise when we have 2 sticks
            # with the same height, in that case, we can confirm that changing
            # any of the index will bring us the same area anyway.
            # Let's assume the heights are -> ..49..24..
            # In this case when start and end are both at 4, and we change either
            # of the indices, the area decreases, and maxArea remains the same.
            # Because area is calculated on the min of heights. So area will never
            # increase. Because 4 still remains as one of the heights.
            # So to change the area, both directions have to have higher heights like -> ..49..84..
            # In this case, no matter which direction we choose in the draw,
            # in the next iteration itself we get on the right track.
            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1

        return max_area


sol = Solution()
assert sol.maxArea2(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert sol.maxArea2(height=[1, 1]) == 1
