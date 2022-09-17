# https://leetcode.com/problems/number-of-longest-increasing-subsequence/discuss/107320/Python-DP-with-explanation-(Beats-88)
class Solution(object):
    # Runtime: 5757 ms, faster than 5.03% of Python3 online submissions for Number of Longest Increasing Subsequence.
    # Memory Usage: 14.3 MB, less than 28.53% of Python3 online submissions for Number of Longest Increasing Subsequence.
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(n^2)
        # Space: O(n)
        dp, longest = [[1, 1] for i in range(len(nums))], 1
        for i, num in enumerate(nums):
            curr_longest, count = 1, 0
            for j in range(i):
                if nums[j] < num:
                    curr_longest = max(curr_longest, dp[j][0] + 1)
            for j in range(i):
                if dp[j][0] == curr_longest - 1 and nums[j] < num:
                    count += dp[j][1]
            dp[i] = [curr_longest, max(count, dp[i][1])]
            longest = max(curr_longest, longest)
        return sum([item[1] for item in dp if item[0] == longest])
