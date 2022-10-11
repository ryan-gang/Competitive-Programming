from typing import List


class Solution:
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

    # Runtime: 1356 ms, faster than 34.09% of Python3 online submissions.
    # Memory Usage: 24.7 MB, less than 48.78% of Python3 online submissions.
    # T : O(N), S : O(1)
    # Ref : discuss/270884/Python-2-solutions%3A-Right-So-Far-One-pass-O(1)-Space-Clean-and-Concise
    def increasingTriplet(self, nums: List[int]) -> bool:
        i = j = float("inf")
        # i and j are the first 2 elements of the triplet.
        # Triplet : i <= j <= k.
        # And i has to come before j. And j has to come before k.
        for num in nums:
            if num <= i:
                # num lte i, we can make this i then.
                # Theoretically we should change j also here, as j has to come after i,
                # but we need to understand, that for the previous value of i, j is still valid.
                # So if we find a k, before changing j, the output can be old_i, j, k.
                # If we update j before finding k then we are golden.
                i = num
            elif num <= j:
                # num lte j, update j to num.
                j = num
            else:
                # num > i and num > j.
                # We have found our triplet !
                return True
        return False


if __name__ == "__main__":
    sol = Solution()
    assert sol.increasingTriplet(nums=[1, 2, 3, 4, 5])
    assert not sol.increasingTriplet(nums=[5, 4, 3, 2, 1])
    assert sol.increasingTriplet(nums=[2, 1, 5, 0, 4, 6])
