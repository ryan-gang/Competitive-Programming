from functools import cache


class Solution:
    """
    At every iteration, we make all the jumps possible from current index, and keep track of the
    number of jumps made in THIS specific jump path.
    When we reach the end, keep track of the min number of jumps."""

    # 95/109 TC Passed. TLE.
    # T : O(N!), S : O(N)
    # At each index i we have N-i choices and we recursively explore each of them till end.
    # So we require O(N*(N-1)*(N-2)...1) = O(N!).
    # O(N) space for the call stack space.
    # But using the cache, reduces the time complexity to O(N^2), only this many unique calls.
    def jumpRecursive(self, nums):
        self.min_jumps = float("inf")
        N = len(nums)

        @cache
        def dfs(idx, jumps):
            if idx >= N - 1:
                self.min_jumps = min(self.min_jumps, jumps)
                return
            for j in range(1, nums[idx] + 1):
                dfs(idx + j, jumps + 1)

        dfs(0, 0)
        return self.min_jumps

    """
    We start from the end, and iteratively calculate the (min) number of jumps required to reach
    upto here. (From the back). Finally return the ans for idx = 0
    We have come to idx "i", with jumps "j", now we can go to the "parent" of idx "i"
    (from where we actually come here in the forward pass) in "j" + 1 jumps.
    We keep on doing this for all indices.
    """
    # T : O(N^2), S : O(N)
    def jumpQuadratic(self, nums):
        n = len(nums)
        dp = [float("inf") for _ in range(n)]
        dp[-1] = 0
        for idx in range(n - 1, -1, -1):
            for j in range(1, nums[idx] + 1):
                jump_idx = min(n - 1, idx + j)
                dp[idx] = min(dp[idx], 1 + dp[jump_idx])
        return dp[0]

    """
    curr is the current position we are standing on.
    (Where we have jumped to, this is constant, unless we jump again)
    idx is the array iteration index.
    farthest is the farthest we can jump to from current index.
    We ALWAYS need to stay ahead of the idx, if it catches us we jump to the farthest possible
    position, (increment jumps). And stay there. Until idx again catches up. While idx is coming
    for us, farthest also keeps on updating and actually keeping track of "farthest".

    We are mario, the idx is the train coming towards us, stay at index for as long as possible,
    but if train has caught up, jump to the farthest.
    """
    # Runtime: 278 ms, faster than 48.38% of Python3 online submissions.
    # Memory Usage: 15 MB, less than 57.51% of Python3 online submissions.
    # T : O(N), S : O(1)
    def jump(self, nums):
        n = len(nums)
        idx = curr = farthest = jumps = 0
        while curr < n - 1:
            farthest = max(farthest, idx + nums[idx])
            if idx == curr:
                curr = farthest
                jumps += 1
            idx += 1

        return jumps


sol = Solution()
assert sol.jump(nums=[2, 3, 1, 1, 4]) == 2
assert sol.jump(nums=[2, 3, 0, 1, 4]) == 2
assert sol.jump(nums=[1]) == 0
assert sol.jump(nums=[1, 2]) == 1
assert sol.jump(nums=[2, 2, 1]) == 1


# Ref : https://leetcode.com/problems/jump-game-ii/
# discuss/1192401/Easy-Solutions-w-Explanation-or-Optimizations-from-Brute-Force-to-DP-to-Greedy-BFS
