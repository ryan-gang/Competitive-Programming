class Solution:
    # 71 / 109 TC passed. TLE.
    # TLE on : nums=[5,6,5,3,9,8,3,1,2,8,2,4,8,3,9,1,0,9,4,6,5,9,8,7,4,2,1,0,2]
    def jump(self, nums):
        self.optimal = float("inf")

        def jump_helper(idx, count):
            if idx >= len(nums) - 1:
                self.optimal = min(self.optimal, count)
                return
            for length in range(1, nums[idx] + 1):
                jump_helper(idx + length, count + 1)

        jump_helper(0, 0)
        return self.optimal


sol = Solution()
assert sol.jump(nums=[2, 3, 1, 1, 4]) == 2
assert sol.jump(nums=[2, 3, 0, 1, 4]) == 2
assert sol.jump(nums=[1]) == 0
assert sol.jump(nums=[1, 2]) == 1
assert sol.jump(nums=[2, 2, 1]) == 1
