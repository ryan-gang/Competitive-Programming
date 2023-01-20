from typing import List, Set, Tuple


class Solution:
    # Runtime: 214 ms, faster than 95.78%.
    # Memory Usage: 22.3 MB, less than 40.47%.
    # T : O(2^N * N), S : O(N)
    # O(N) for converting list to tuples and adding to set, for 2^N subsequences.
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        all_seqs: Set[Tuple[int]] = set()

        def traverse(seq: List[int], idx: int):
            """index idx, will be processed now."""
            if len(seq) > 1:
                all_seqs.add(tuple(seq))
            for i in range(idx, n):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                if seq and nums[i] < seq[-1]:
                    continue
                seq.append(nums[i])
                traverse(seq, i + 1)
                seq.pop()

        traverse([], 0)
        return all_seqs


if __name__ == "__main__":
    sol = Solution()
    print(sol.findSubsequences(nums=[4, 6, 7, 7]))
    # print(sol.findSubsequences(nums=[4, 4, 3, 2, 1]))
    # print(sol.findSubsequences(nums=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1, 1, 1]))
    # print(sol.findSubsequences(nums=[1, 1, 5, 5, 1, 1]))
