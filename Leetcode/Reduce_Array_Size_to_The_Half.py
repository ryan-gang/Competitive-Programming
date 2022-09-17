from collections import Counter
from typing import List


class Solution:
    # 1132 ms, faster than 27.95% of Python3 online submissions.
    # Memory Usage: 35.3 MB, less than 50.95% of Python3 online submissions.
    # T : O(NlogN), S : O(N)
    def minSetSize(self, arr: List[int]) -> int:
        d = Counter(arr)
        # Sorted_d is also extra space consuming. Not required.
        sorted_d = sorted(d.items(), key=lambda item: item[1], reverse=True)
        count = 0
        length = len(arr)
        while length > len(arr) // 2:
            length -= sorted_d[count][1]
            count += 1

        return count

    def minSetSizePartiallyBetter(self, nums: List[int]) -> int:
        count = Counter(nums)
        totalFrequency, size = 0, 0
        # Less space requirement.
        for frequency in sorted(count.values(), reverse=True):
            totalFrequency += frequency
            size += 1
            if totalFrequency >= len(nums) // 2:
                break

        return size

    # T : O(N), S : O(N)
    def minSetSizeBetter(self, arr: List[int]) -> int:
        n = len(arr)
        cnt = Counter(arr)

        # Counting sort.
        # Sorts in O(N) time, but O(N) space requirement.
        counting = [0] * (n + 1)
        for freq in cnt.values():
            counting[freq] += 1

        ans, removed, half, freq = 0, 0, n // 2, n
        while removed < half:
            ans += 1
            while counting[freq] == 0:
                freq -= 1
            removed += freq
            counting[freq] -= 1
        return ans


sol = Solution()
assert sol.minSetSize(arr=[3, 3, 3, 3, 5, 5, 5, 2, 2, 7]) == 2
assert sol.minSetSize(arr=[7, 7, 7, 7, 7, 7]) == 1
