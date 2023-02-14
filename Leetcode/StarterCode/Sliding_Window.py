"""
Startercode for sliding window core.
"""
from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        baskets: dict[int, int] = defaultdict()
        left = right = max_num = 0
        K = 2

        while right < len(fruits):
            # 1) add a new value to the sliding window
            baskets[fruits[right]] += 1
            right += 1
            # 1.1) increase right immediately
            # 2) 'repair' the window if it violates the constraints
            while len(baskets) > K:
                baskets[fruits[left]] -= 1
                # remove a value from the sliding window
                if baskets[fruits[left]] == 0:
                    del baskets[fruits[left]]
                left += 1
            # 3) at this point you know that your sliding window is always valid
            # check condition min/max/whatever
            # here you already have proper count

            max_num = max(max_num, right - left)

        return max_num
