from typing import List


class Solution:
    """
    Instead of searching the entire rest of the array,
    when a larger element than `j` is not found.
    We instead ignore current `i` and `j` and start afresh. This smaller element is now `i` or `j`.
    And we continue our search.
    Reducing worst case time complexity from O(N^3) to O(N)
    """

    # Brute force solution.
    # 75 / 76 TC passed. TLE.
    # T : O(N^3), S : O(1)
    def increasingTripletNaieve(self, nums: List[int]) -> bool:
        n = len(nums)
        # out = []
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    for k in range(j + 1, n):
                        if nums[j] < nums[k]:
                            # out.append((nums[i], nums[j], nums[k]))
                            return True

        return False

    # Runtime: 1350 ms, faster than 13.87% of Python3 online submissions.
    # Memory Usage: 24.8 MB, less than 18.45% of Python3 online submissions.
    # T : O(N), S : O(1)
    def increasingTriplet(self, nums: List[int]) -> bool:
        i = j = float("inf")
        for num in nums:
            if num <= i:
                i = num
            elif num <= j:
                j = num
            else:
                return True
        return False


sol = Solution()
assert sol.increasingTriplet(nums=[1, 2, 3, 4, 5])
assert not sol.increasingTriplet(nums=[5, 4, 3, 2, 1])
assert sol.increasingTriplet(nums=[2, 1, 5, 0, 4, 6])
