from bisect import bisect_left
from typing import List


class Solution:
    # Not Required, use bisect_left().
    @staticmethod
    def insertPosition(val: int, nums: List[int]):
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == val:
                return mid
            elif nums[mid] > val:
                hi = mid - 1
            else:
                lo = mid + 1

        return lo

    # Runtime: 112 ms, faster than 87.56% of Python3 online submissions.
    # Memory Usage: 14.3 MB, less than 47.45% of Python3 online submissions.
    # T : O(NLogN), S : O(N)
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        The core idea of this algo is :
        If our current LIS array is : [2, 3, 7, 8] and we come across a new element 4,
        instead of discarding it or creating a new array with it at its centre, we will
        try to accomodate it in our current array.
        Finding the proper index of the element, and inserting it there, so in this case
        it would be : [2, 3, 4, 8]
        If later on we find a greater element than 8, we can append to the end of our out array.
        Because it is not disturbing our length calculation, if we had not done
        the previous swap our length would have been same.
        If we find another element greater than 4 but less than 8, we can again swap with 8.
        """
        out: List[int] = []
        out.append(nums[0])
        for i in nums:
            if i > out[-1]:
                out.append(i)
            else:
                # idx = Solution.insertPosition(i, out)
                idx = bisect_left(out, i)
                out[idx] = i

        return len(out)


class SolutionDP:
    """
    Backtracking concept.
    Every element can be either ignored, or if it is greater than the last element in seq,
    can be added to the sequence.
    We generate all subsequences.
    And then keep a track of the maximum length LIS.
    """

    # 22 / 54 TC passed. TLE.
    def backtrack(self, nums: List[int]):
        N = len(nums)
        self.max_length = 0

        def dfs(idx: int, seq: List[int], length: int):
            if idx == (N):
                self.max_length = max(self.max_length, length)
                return
            dfs(idx + 1, seq, length)  # idx element is ignored.
            if seq == [] or nums[idx] > seq[-1]:
                dfs(idx + 1, seq + [nums[idx]], length + 1)

        dfs(0, [], 0)
        return self.max_length

    """
    dp[i] is the length of LIS ending at ith index. So at least, it has to be 1.
    Check every element before this, if this number is more than nums[i],
    We can extend that LIS, by appending this element to that LIS.
    We store the updated length in dp[i]
    """
    # Ref : Tushar Roy video on LIS.
    # Runtime: 5307 ms, faster than 36.20%.
    # Memory Usage: 14.3 MB, less than 46.86%.
    # T : O(N ^ 2), S : O(N)
    def lengthOfLISDP0(self, nums: List[int]):
        n, max_length = len(nums), 1
        dp = [1 for _ in range(n)]
        for i in range(1, n):
            for j in range(i + 1):
                if nums[i] > nums[i - j]:
                    dp[i] = max(dp[i], 1 + dp[i - j])
            max_length = max(max_length, dp[i])
        return max_length

    # Runtime: 3582 ms, faster than 56.68%.
    # Memory Usage: 14.2 MB, less than 81.29%.
    # T : O(N ^ 2), S : O(N)
    def lengthOfLISDP(self, nums: List[int]):
        """Same idea, straight forward implementation."""
        n = len(nums)
        dp = [1 for _ in range(n)]

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


if __name__ == "__main__":
    sol = Solution()
    assert (sol.lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18])) == 4
    assert (sol.lengthOfLIS(nums=[0, 1, 0, 3, 2, 3])) == 4
    assert (sol.lengthOfLIS(nums=[7, 7, 7, 7, 7, 7, 7])) == 1
