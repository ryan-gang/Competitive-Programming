import bisect
import math
from typing import List


class SolutionWrong:
    # This returns all subarrays.
    # But we need only contiguos subarrays.
    def helper(self, nums, k):
        self.all, self.nums, self.k = [], nums, k
        self.out = []
        self.recurse(0, [], 1)
        return len(self.out)

    def recurse(self, next_i, curr_array, curr_product):
        if curr_product < k:
            if curr_array:
                self.out.append(curr_array[::])
        else:
            return
        for i in range(next_i, len(self.nums)):
            self.recurse(i + 1, curr_array + [self.nums[i]], curr_product * self.nums[i])

    # This returns all subarrays.
    # But we need only contiguos subarrays.
    def recurse2(self, next_i, curr_array, curr_product):
        if curr_product < self.k:
            if curr_array:
                self.out.append(curr_array[::])
        else:
            return False
        for i in range(next_i, len(self.nums)):
            val = self.recurse2(i + 1, curr_array + [self.nums[i]], curr_product * self.nums[i])
            if val is False:
                return


# 72/97 TC passed. MemoryLimitExceeded (Recursion Depth reached).
class SolutionRecurse:
    # def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
    #     self.all, self.nums, self.k = [], nums, k
    #     for i in range(len(nums)):
    #         self.recurse([], i, 1)

    #     return len(self.all)

    # def recurse(self, array, idx, product):
    #     new_product = product * self.nums[idx]
    #     if new_product >= self.k:
    #         return
    #     array.append(self.nums[idx])
    #     if array:
    #         self.all.append(array[::])
    #     if idx + 1 < len(self.nums):
    #         self.recurse(array, idx + 1, new_product)
    #         array.pop()

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        self.all, self.nums, self.k = 0, nums, k
        for i in range(len(nums)):
            self.recurse([], i, 1)

        return self.all

    def recurse(self, array, idx, product):
        new_product = product * self.nums[idx]
        if new_product >= self.k:
            return
        array.append(self.nums[idx])
        if array:
            self.all += 1
        if idx + 1 < len(self.nums):
            self.recurse(array, idx + 1, new_product)
            array.pop()


class Solution:
    # Runtime: 1572 ms, faster than 6.91% of Python3 online submissions.
    # Memory Usage: 16.8 MB, less than 15.34% of Python3 online submissions.
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count, product, left = 0, 1, 0
        # For every index in nums, find the earliest index from where running
        # product upto here is less than k.
        for right, val in enumerate(nums):
            print(right, left)
            product *= val
            while product >= k:
                product /= nums[left]
                left += 1
            # For every index, we add the count of subarrays, ending with this index.
            # If nums = [10, 2, 5, 6]
            # i = 1, subarrays = [10]
            # i = 2, subarrays = [2], [10, 2]
            # i = 3, subarrays = [5], [2, 5], [10, 2, 5]
            # And so on.
            count += right - left + 1

        return count

    def numSubarrayProductLessThanKLog(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        k = math.log(k)
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + math.log(x))
        ans = 0
        for lo, x in enumerate(prefix):
            # hi is the index, where x+k can be inserted in a sorted array, prefix in this case.
            # Binary Search will start from lo+1.
            hi = bisect.bisect(prefix, x + k - 1e-9, lo + 1)
            ans += hi - lo - 1
        return ans


sol = Solution()
print(sol.numSubarrayProductLessThanK(nums=[10, 5, 2, 6], k=100))
print(sol.numSubarrayProductLessThanK(nums=[1, 2, 3], k=0))
