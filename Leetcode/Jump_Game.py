from typing import List


class Solution:
    # Runtime: 1356 ms, faster than 13.07% of Python3 online submissions.
    # Memory Usage: 15.1 MB, less than 96.73% of Python3 online submissions.
    def canJump2(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        dp = [0 for _ in range(n)]
        for i in range(0, n - 1):
            tmp = max(dp[i - 1] - 1, nums[i])
            if tmp < 1:
                return False
            dp[i] = tmp
        return True

    # Runtime: 1341 ms, faster than 16.51% of Python3 online submissions.
    # Memory Usage: 15.1 MB, less than 81.41% of Python3 online submissions.
    def canJump1(self, nums: List[int]) -> bool:
        """
        The idea is that, for every index in the array, we keep track of how far we can go from
        THAT index. So it depends on nums[idx] and dp[idx] which in turn depends on the previous
        indices of nums. Basically if we have a big number, this will keep on lingering in the dp
        array, reducing by 1 every iteration. We keep the max of dp[i] and nums[i], so even if
        nums[i] is low, dp[i] can carry us forward."""
        n = len(nums)
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        for i in range(1, n):
            if dp[i - 1] < 0:
                return False
            dp[i] = max(dp[i - 1], nums[i - 1]) - 1
        return dp[n - 1] >= 0

    # Runtime: 1688 ms, faster than 10.81%.
    # Memory Usage: 15.2 MB, less than 82.26%.
    # T : O(N), S : O(1)
    def canJump(self, nums: List[int]) -> bool:
        """
        Similar idea like the previous one, we just lose the dp.
        We keep track of the furthest index we can go from here, in the max_range variable.
        And we update that every iteration.
        If it goes to 0, we can't go further.
        """
        max_range, idx, n = 1, 0, len(nums)

        while idx < n and max_range > 0:
            max_range -= 1
            max_range = max(max_range, nums[idx])
            idx += 1

        return idx == len(nums)

    # Runtime:519 ms, faster than 83.88%.
    # Memory Usage: 15.1 MB, less than 97.51%.
    # T : O(N), S : O(1)
    def canJump3(self, nums: List[int]) -> bool:
        max_range = nums[0]
        for idx, jump in enumerate(nums[1:]):
            if max_range == 0:
                # If we can't jump anymore, return if we are at the end of the array.
                return idx == len(nums) - 1
            max_range -= 1  # Else, reduce range by 1.
            max_range = max(max_range, jump)  # Update range with the current jump value.

        # Finally return if we have reached the end with range >= 0.
        return max_range >= 0


if __name__ == "__main__":
    sol = Solution()
    assert sol.canJump(nums=[2, 3, 1, 1, 4])
    assert not sol.canJump(nums=[3, 2, 1, 0, 4])
    assert sol.canJump(nums=[0])
    assert sol.canJump(nums=[2])
    assert not sol.canJump(nums=[0, 2, 3])
    assert sol.canJump(nums=[2, 0, 0])
    assert sol.canJump(nums=[1, 2, 3])
    assert not sol.canJump(nums=[0, 1])
