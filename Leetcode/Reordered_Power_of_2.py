import collections
import itertools


class Solution:
    # Runtime: 79 ms, faster than 31.55% of Python3 online submissions.
    # Memory Usage: 13.9 MB, less than 64.17% of Python3 online submissions.
    # T : O(N), S : O(1)
    # Create a set of all possible powers, and sort them.
    # Now after getting an input, sort it and check if it is in the set.
    def __init__(self) -> None:
        self.powers = set()
        for i in range(33):
            val = str(2**i)
            val = "".join(sorted(val))
            self.powers.add(val)

    def reorderedPowerOf2(self, n: int) -> bool:
        n = "".join(sorted(str(n)))
        return n in self.powers

    # TLE : 124 / 136 test cases passed.
    # Creating all permutations myself.
    def reorderedPowerOf2TLE(self, n: int) -> bool:
        self.flag = False

        def helper(nums, permutation):
            if not nums:
                if not permutation.startswith("0"):
                    val = int(permutation)
                    if bin(val).count("1") == 1:
                        self.flag = True
            for i in range(len(nums)):
                helper(nums[:i] + nums[i + 1:], permutation + nums[i])

        helper(str(n), "")

        return self.flag

    # Creating permutations, using itertools.permutations()
    def reorderedPowerOf2Permutations(self, n: int) -> bool:
        return any(
            cand[0] != "0" and bin(int("".join(cand))).count("1") == 1
            for cand in itertools.permutations(str(n))
        )

    def reorderedPowerOf2Counter(self, N):
        count = collections.Counter(str(N))
        return any(count == collections.Counter(str(1 << b)) for b in range(31))


sol = Solution()
print(sol.reorderedPowerOf2(n=1))
assert sol.reorderedPowerOf2(n=1)
assert not sol.reorderedPowerOf2(n=10)
