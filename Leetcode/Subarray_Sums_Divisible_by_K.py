from collections import defaultdict
from math import comb
from typing import Dict, List


class Solution:
    def subarraysDivByKBruteForce(self, nums: List[int], k: int) -> int:
        count, n = 0, len(nums)
        out: List[List[int]] = []
        for i in range(n):
            for j in range(i, n):
                subarray = nums[i : j + 1]
                if sum(subarray) % k == 0:
                    out.append(subarray)
                    count += 1
                    print(subarray)

        return count

    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count, n = 0, len(nums)
        pre = [nums[0]]
        for i in nums[1:]:
            pre.append(pre[-1] + i)
        for i in range(n):
            for j in range(i, n):
                prev = pre[i - 1] if i > 0 else 0
                sum_subarray = pre[j] - prev
                if sum_subarray % k == 0:
                    count += 1
        return count

    def subarraysDivByKOptimal(self, nums: List[int], k: int) -> int:
        running = total = 0
        d: Dict[int, int] = defaultdict(int)
        d[0] += 1
        for num in nums:
            running += num
            d[running % k] += 1
        for key in d:
            if d[key] > 1:
                total += comb(d[key], 2)
        return total


if __name__ == "__main__":
    sol = Solution()
    print(sol.subarraysDivByKOptimal(nums=[4, 5, 0, -2, -3, 1], k=5))
