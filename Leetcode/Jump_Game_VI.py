from collections import deque
from typing import List
import heapq


class Solution:
    # 57/71 passed, TLE.
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            start = max(0, i - k)
            Z = dp[start : i - 1 + 1]  # noqa : E203
            # These 2 lines, are making the code slow.
            # Slicing is basically copying into a new list.
            # Then traversing the entire thing to find max.
            prev_max_value = max(Z)
            dp[i] = prev_max_value + nums[i]

        return dp[-1]

    # 57/71 passed, Unfortunate Python bug. :(
    # heapq doesn't guarantee sorted order of the underlying heap.
    def maxResultOptimal(self, nums: List[int], k: int) -> int:
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]

        # Custom comparator for heap ->
        # def new_cmp_lt(self, a, b):
        #     return a[0] < b[0]
        # heapq.cmp_lt = new_cmp_lt

        heap = []
        # heap items will be -val, index, heap order will be based on val
        heapq.heappush(heap, (-nums[0], 0))

        for i in range(1, len(nums)):
            start = max(0, i - k)
            # print(heap)
            index = 0
            while (heap[index][1]) < start:
                # Getting the largest dp value, within the last i-k element.
                # V[1] has to be greater than i - k.
                # Else increment index, get other high number.
                index += 1
            V = heap[index]
            prev_max_value = -V[0]
            dp[i] = prev_max_value + nums[i]
            heapq.heappush(heap, (-dp[i], (i)))
            print(i, (-V[0], V[1]))

        return dp[-1]

    # Runtime: 1579 ms, faster than 49.44% of Python3 online submissions for Jump Game VI.
    # Memory Usage: 27.6 MB, less than 66.77% of Python3 online submissions for Jump Game VI.
    def maxResultPDeque(self, nums: List[int], k: int) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        # Create DP array, with all zeros. Initialize with value for 0th idx.
        d = deque([(nums[0], 0)])
        # Push 0th idx value to deque also.
        for i in range(1, len(nums)):
            # d[0] will always be the largest value of the last k dp entries.
            dp[i] = nums[i] + d[0][0]
            # If deque contains any value <= dp[i] it has to be removed,
            # the lower values will never be used anyway. Plus it will
            # break out sort. Always removing the smaller numbers will
            # make the larger values bubble to the top.
            while d and d[-1][0] < dp[i]:
                d.pop()
            # Append current dp entry to deque.
            # deque is sorted here BTW, all vals less than dp[i] have been removed.
            # Either dp[i] is largest, or some other large value is infront of dp[i]
            d.append((dp[i], i))
            # If the largest values (dp[0]) have occured before i - k idxs,
            # it have to be removed. They can't be used.
            if i - k == d[0][1]:
                d.popleft()
        return dp[-1]


# nums, k = [1, -5, -20, 4, -1, 3, -6, -3], 2
# nums, k = [10, -5, -2, 4, 0, 3], 3
# nums, k = [1, -1, -2, 4, -7, 3], 2
# nums, k = [-1, -2, -3], 4
# nums, k = [100, -1, -100, -1, 100], 2
