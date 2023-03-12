class Solution:
    """
    Here we need to maximise the number of indices in the prefix sum which have value > 0.
    To do this all the positive number should be at the begining, so that we accumulate
    the greatest possible sum, and then add all the negative numbers, so that the first few
    negative numbers still lead to a positive value in the prefix sum.
    We just need to sort it in reverse, and start adding the elements and count it
    until we get the sum as -ve or zero.
    """

    # T : O(N), S : O(1)
    def maxScore(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        val = score = 0
        for i in nums:
            val += i
            if val > 0:
                score += 1
            else:
                # val is the prefix sum, if it goes <= 0. It means we have encountered negative
                # values. And values in the coming iterations will only go lower. So we can
                # break out of the loop.
                break
        return score


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxScore(nums=[2, -1, 0, 1, -3, 3, -3]) == 6
    assert sol.maxScore(nums=[-2, -3, 0]) == 0
