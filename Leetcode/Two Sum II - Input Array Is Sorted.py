from collections import defaultdict
from typing import List


# Runtime: 267 ms, faster than 10.96% of Python3 online submissions...
# Memory Usage: 14.9 MB, less than 41.52% of Python3 online submissions...
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < len(numbers) and j >= 0:
            val = numbers[i] + numbers[j]
            if val < target:
                i += 1
            elif val > target:
                j -= 1
            else:
                return [i + 1, j + 1]


# Runtime: 130 ms, faster than 93.60% of Python3 online submissions...
# Memory Usage: 15.1 MB, less than 11.40% of Python3 online submissions...
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(numbers)):
            num = numbers[i]
            if target - num in d:
                return [d[target - num] + 1, i + 1]
            d[num] = i
        return None


numbers = [2, 3, 4]
target = 6

# BINARY SEARCH IS NOT WORKING TODO
def binarySearch(val, array):
    lo, hi = 0, len(array) - 1
    mid = (lo + hi) // 2
    while lo < hi:
        if array[mid] > val:
            hi = mid - 1
        elif array[mid] < val:
            lo = mid + 1
        else:
            return mid


for i in range(len(numbers)):
    num = numbers[i]
    index = binarySearch(target - num, numbers)
    if index:
        if index != i:
            if numbers[index] + num == target:
                out = [index + 1, i + 1]
                out.sort()
                print(out)
                break

print(binarySearch(4, numbers))
