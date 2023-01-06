from typing import List


class Solution:
    # Runtime: 2611 ms, faster than 6.28%.
    # Memory Usage: 27.9 MB, less than 61.26%.
    # T : O(NLogN), S : O(N) (for sorting)
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        bill = idx = 0
        while idx < len(costs):
            bill += costs[idx]
            if bill <= coins:
                idx += 1
            else:
                break
        return idx

    # Using Counting sort.
    # T : O(N + M), N = len, M = max.
    # S : O(M)
    def maxIceCream1(self, costs: List[int], coins: int) -> int:
        _, icecreams = len(costs), 0
        m = max(costs)

        costsFrequency = [0] * (m + 1)
        for cost in costs:
            costsFrequency[cost] += 1

        for cost in range(1, m + 1):
            # No ice cream is present costing 'cost'.
            if not costsFrequency[cost]:
                continue
            # We don't have enough 'coins' to even pick one ice cream.
            if coins < cost:
                break

            # Count how many icecreams of 'cost' we can pick with our 'coins'.
            # Either we can pick all ice creams of 'cost' or we will be limited by remaining coins.
            count = min(costsFrequency[cost], coins // cost)
            # We reduce price of picked ice creams from our coins.
            coins -= cost * count
            icecreams += count

        return icecreams
