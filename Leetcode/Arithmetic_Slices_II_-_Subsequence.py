from collections import defaultdict


class Solution:
    # TLE.
    # T : O(2 ^ N), S : O(N)
    def numberOfArithmeticSlicesTLE(self, nums: list[int]) -> int:
        N = len(nums)
        out: list[list[int]] = []

        def dfs(seq: list[int], index: int, diff: int):
            if len(seq) >= 3:
                out.append(seq[:])
            for i in range(index, N):
                val = nums[i]
                if len(seq) == 0:
                    dfs(seq + [val], i + 1, diff=0)
                elif len(seq) == 1:
                    dfs(seq + [val], i + 1, diff=val - seq[-1])
                else:
                    if val - seq[-1] == diff:
                        dfs(seq + [val], i + 1, val - seq[-1])

        dfs([], 0, 0)
        return len(out)

    # Runtime: 1055 ms, faster than 31.17%.
    # Memory Usage: 68.8 MB, less than 23.9%.
    # T : O(N^2), S : O(N^2)
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        """
        Let dp[j][diff] be the count of slices ending at A[j], with diff as common difference.
        If we want to add A[i] to any of the existing slices, we need to make sure the common
        difference matches. So, dp[i][diff] += dp[j][diff]
        But as the basic state is 0. All states will then be 0.
        We need to introduce weak arithmetic slices, arithmetic slices of length >= 2.
        So, for weak slices : dp[i][diff] += (dp[j][diff] + 1)
        Because (i, j) themselves create a weak slice.
        But now we are counting all weak slices. But output should contain only slices of
        length >= 3. We can
        1. Count all weak slices, subtract slices of length = 2.
        2. Keep a running count of only valid slices.
        At every iteration dp[j][diff] is the count of all valid slices,
        1 is the only invalid slice (of length == 2).
        """
        n = len(nums)
        dp: list[dict[int, int]] = [defaultdict(int) for _ in range(n)]
        slices = 0

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += dp[j][diff] + 1
                slices += dp[j][diff]

        return slices

    def numberOfArithmeticSlices2(self, nums: list[int]) -> int:
        n = len(nums)
        dp: list[dict[int, int]] = [defaultdict(int) for _ in range(n)]

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += dp[j][diff] + 1

        total_slices = 0
        for idx in dp:
            for diff in idx:
                total_slices += idx[diff]

        pure_weak_slices = n * (n - 1) / 2
        return int(total_slices - pure_weak_slices)


if __name__ == "__main__":
    sol = Solution()
    assert sol.numberOfArithmeticSlices(nums=[2, 4, 6, 8, 10]) == 7
    assert sol.numberOfArithmeticSlices(nums=[7, 7, 7, 7, 7]) == 16
    assert sol.numberOfArithmeticSlices2(nums=[1]) == 0
    assert (
        sol.numberOfArithmeticSlices(
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        )
    ) == 2096920
