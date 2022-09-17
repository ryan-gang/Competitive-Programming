from typing import List


class Solution:
    # 71 / 211 TC passed. TLE.
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        out = []

        # i has not been computed upon.
        def recurse(i, array, sum):
            if len(array) == 4:
                if array[-1] == sum - array[-1]:
                    out.append(array[:])
                    return
            for j in range(i, n):
                array.append(nums[j])
                recurse(j + 1, array, sum + nums[j])
                array.pop()

        recurse(0, [], 0)
        return len(out)


sol = Solution()
assert sol.countQuadruplets(nums=[1, 1, 1, 1]) == 0
assert sol.countQuadruplets(nums=[1, 2, 3, 6]) == 1
assert sol.countQuadruplets(nums=[3, 3, 6, 4, 5]) == 0
assert sol.countQuadruplets(nums=[1, 1, 1, 3, 5]) == 4
