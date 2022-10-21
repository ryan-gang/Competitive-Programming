import collections
from typing import List


class Solution:
    # Runtime: 2165 ms, faster than 5.01% of Python3 online submissions.
    # Memory Usage: 33.6 MB, less than 5.45% of Python3 online submissions.
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = collections.defaultdict(list)

        for idx, val in enumerate(nums):
            d[val].append(idx)

        for key in d:
            val = d[key]
            val.sort()
            for _ in range(len(val) - 1):
                if val[_ + 1] - val[_] <= k:
                    return True

        return False

    # Runtime: 2195 ms, faster than 5.01% of Python3 online submissions.
    # Memory Usage: 27.4 MB, less than 32.52% of Python3 online submissions.
    def containsNearbyDuplicate2(self, nums: List[int], k: int) -> bool:
        d = {}
        # No need to keep ALL the indices, only the latest one will suffice.
        # Because this difference only has the best chance of coming below k.

        for idx, val in enumerate(nums):
            if val in d and idx - d[val] <= k:
                return True
            d[val] = idx

        return False

    # We can further optimise the code by keeping a "cache" of the most recent k
    # elements and checking if our current val is in the cache or not, that way we
    # can return at once. And we regularly prune the older elements from the cache.
    # Runtime: 659 ms, faster than 89.40% of Python3 online submissions.
    # Memory Usage: 25.4 MB, less than 91.51% of Python3 online submissions.
    def containsNearbyDuplicate3(self, nums: List[int], k: int) -> bool:
        seen = set()
        for idx, val in enumerate(nums):
            if val in seen:
                return True
            seen.add(val)
            if len(seen) > k:
                seen.remove(nums[idx - k])

        # 0, 1, [2, 3, 4, 5], 6, 7, 8, 9, 10
        # idx = 5, k = 4, window will end at idx = 5, and will be of length = 4.
        # Remove element at index = idx - k
        return False


if __name__ == "__main__":
    sol = Solution()
    assert sol.containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3)
    assert not sol.containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2)
    assert sol.containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1)
