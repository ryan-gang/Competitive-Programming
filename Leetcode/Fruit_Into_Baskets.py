from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        # We use a hash map 'basket' to store the number of each type of fruit.
        basket: dict[int, int] = defaultdict(int)
        max_picked = 0
        left = 0

        # Add fruit from the right index (right) of the window.
        for right in range(len(fruits)):
            basket[fruits[right]] += 1

            # If the current window has more than 2 types of fruit,
            # we remove fruit from the left index (left) of the window,
            # until the window has only 2 types of fruit.
            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1

            # Update max_picked.
            max_picked = max(max_picked, right - left + 1)

        # Return max_picked as the maximum number of fruits we can collect.
        return max_picked

    # Runtime: 1013 ms, faster than 59.86%.
    # Memory Usage: 20 MB, less than 80.52%.
    # T : O(N), S : O(1)
    def totalFruit1(self, fruits: list[int]) -> int:
        n = len(fruits)
        left = right = max_fruits = 0
        basket: dict[int, int] = defaultdict(int)
        K = 2

        while right < n:
            fruit = fruits[right]
            basket[fruit] += 1

            while len(basket) > K:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1

            max_fruits = max(max_fruits, right - left + 1)
            right += 1

        return max_fruits

    # Runtime: 935 ms, faster than 64.47%.
    # Memory Usage: 20.2 MB, less than 53.11%.
    # T : O(N), S : O(N)
    def totalFruit2(self, fruits: list[int]) -> int:
        k = 2
        d: dict[int, int] = defaultdict(int)
        count = max_count = 0
        lo = hi = 0
        n = len(fruits)

        while hi < n:
            while hi < n and len(d) <= k:
                fruit = fruits[hi]
                d[fruit] += 1
                hi += 1
            count = hi - lo - 1
            max_count = max(max_count, count)
            while len(d) > k:
                fruit = fruits[lo]
                d[fruit] -= 1
                if d[fruit] == 0:
                    del d[fruit]
                lo += 1
            count = hi - lo
            max_count = max(max_count, count)

        max_count = max(max_count, count)

        return max_count
