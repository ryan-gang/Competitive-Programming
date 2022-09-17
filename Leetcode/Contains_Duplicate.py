from typing import List
from collections import Counter, defaultdict


class Solution:
    # Runtime: 1604 ms, faster than 5.01%.
    # Memory Usage: 25.7 MB, less than 96.45%.
    # Incredibly unoptimised. :(
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = Counter(nums)
        return any(map(lambda x: x > 1, d.values()))

    def containsDuplicate2(self, nums: List[int]) -> bool:
        d = Counter(nums)
        return any(i > 1 for i in d.values())

    def containsDuplicate3(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

    def containsDuplicate4(self, nums: List[int]) -> bool:
        d = Counter(nums)
        return sum(d.values()) > len(d)

    def containsDuplicate5(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        for _, freq in freq.items():
            if freq > 1:
                return True
        return False

    def containsDuplicate6(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False

    # This is arguably the most optimised method.
    # With higher chances of premature completion.
    def containsDuplicate7(self, nums: List[int]) -> bool:
        d = defaultdict(int)
        for i in nums:
            if d[i] > 0:
                return True
            else:
                d[i] += 1
        return False
