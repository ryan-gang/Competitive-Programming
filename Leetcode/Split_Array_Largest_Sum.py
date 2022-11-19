from typing import List


class Solution:
    """
    Ref : discuss/89817/Clear-Explanation%3A-8ms-Binary-Search-Java
    The idea is to run a binary search on the sums of contiguous arrays.
    Try to minimize this value using Binary Search.
    Start from min value possible ie max(array), and sum(array),
    and then binary search for the min value, that allows us to have k subarrays.
    """

    # Runtime: 78 ms, faster than 56.47% of Python3 online submissions.
    # Memory Usage: 14.1 MB, less than 18.64% of Python3 online submissions.
    def splitArray(self, nums: List[int], k: int) -> int:
        lo, hi = max(nums), sum(nums)
        while lo <= hi:
            mid = (lo + hi) // 2
            if Solution.valid_array(array=nums, max_sum=mid, k=k):
                # Try to reduce max_sum if it is valid.
                hi = mid - 1
            else:
                # If not valid, try increasing max_sum.
                lo = mid + 1
        return lo

    @staticmethod
    def valid_array(array: List[int], max_sum: int, k: int) -> bool:
        """Return True if array can be divided into 'k' contiguous subarrays
        with their sum less than or equal to  max_sum"""
        # outer, inner = [], []
        subarrays = 1
        array_sum = 0

        for num in array:
            array_sum += num
            # inner.append(num)
            if array_sum > max_sum:
                # outer.append(inner[:-1])
                # inner = [num]
                array_sum = num
                subarrays += 1
                if subarrays > k:
                    # print(outer, False)
                    return False

        # outer.append(inner)
        # print(outer, subarrays == k)
        """
        Whenever we return False, the splitArray method tries to increase the max_sum to help
        the array accomodate more elements in the subarrays, but in the case where we are short
        of k, it will spiral out right ?
        So we return True, because ultimately we are going to reduce max_sum anway, reduction
        will go on until max_sum = max(array), at which point we might reach our
        single length arrays.
        """
        # return subarrays == k

        return True


if __name__ == "__main__":
    sol = Solution()
    assert (sol.splitArray(nums=[7, 2, 5, 10, 8], k=2)) == 18
    assert sol.splitArray(nums=[1, 2, 3, 4, 5], k=2) == 9
    assert (sol.splitArray([1, 4, 4], 3)) == 4
