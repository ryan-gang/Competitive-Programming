from itertools import accumulate


class Solution:
    # T : O(N), S : O(N)
    def findPrefixScore(self, nums: list[int]) -> list[int]:
        conver = [0] * len(nums)
        ans: list[int] = []

        max_val = 0
        score = 0
        for idx, val in enumerate(nums):
            max_val = max(max_val, val)
            conver[idx] = max_val + nums[idx]
            score += conver[idx]
            ans.append(score)

        return ans

    def findPrefixScore1(self, nums: list[int]) -> list[int]:
        m = 0
        conver: list[int] = []
        for x in nums:
            m = max(m, x)
            conver.append(x + m)
        return list(accumulate(conver))
