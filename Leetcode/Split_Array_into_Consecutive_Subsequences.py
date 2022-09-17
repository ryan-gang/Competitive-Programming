from collections import defaultdict, Counter
from typing import List


class Solution:
    # Runtime: 939 ms, faster than 35.20% of Python3 online submissions.
    # Memory Usage: 15.3 MB, less than 25.22% of Python3 online submissions.
    def isPossible(self, nums: List[int]) -> bool:
        # key: ending number, val: how many seqs
        seq = defaultdict(int)
        # key: number, val: how many of key are left unchecked in nums
        left = Counter(nums)

        for num in nums:
            # With the if condition, we might have exhausted values from nums,
            # while creating a future subsequence.
            # We should not proceed with num, if there is no num left in nums.
            if not left[num]:
                continue
            # There is no subsequence ending with (num - 1)
            if not seq[num - 1]:
                # Check if num + 1 and num + 2 exists.
                # Only then we can create a valid subsequence.
                if left[num + 1] > 0 and left[num + 2] > 0:
                    seq[num + 2] += 1
                    for i in range(3):
                        left[num + i] -= 1
                # Else we do not have a valid solution.
                else:
                    return False
            # There already is a subsequence ending with (num - 1)
            # Append num to the previous subsequence.
            else:
                seq[num - 1] -= 1
                seq[num] += 1
                left[num] -= 1

        return True


sol = Solution()
print(sol.isPossible(nums=[1, 2, 3, 3, 4, 5]))
print(sol.isPossible(nums=[1, 2, 3, 4, 4, 5, 6]))
