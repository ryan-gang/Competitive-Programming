from typing import List
from StarterCode.decorators import timeit

# Ref : https://leetcode.com/problems/combination-sum-iv/discuss/85036/1ms-Java-DP-Solution-with-Detailed-Explanation


class SolutionRecursive:
    @timeit
    def combinationSum4(self, nums: List[int], target: int) -> int:
        return self.helper(nums, target)

    def helper(self, nums: List[int], target: int):
        # num got added to sequence
        if target == 0:
            return 1
        else:
            out = 0
            for i in range(len(nums)):
                if target >= nums[i]:
                    out += self.helper(nums, target - nums[i])
            return out


class SolutionDP:
    # Runtime: 51 ms, faster than 76.73% of Python3 online submissions.
    # Memory Usage: 14 MB, less than 48.19% of Python3 online submissions.
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.dp = [-1 for _ in range(target + 1)]
        self.dp[0] = 1
        return self.helper(nums, target)

    def helper(self, nums: List[int], target: int):
        if self.dp[target] != -1:
            return self.dp[target]
        else:
            out = 0
            for i in range(len(nums)):
                if target >= nums[i]:
                    out += self.helper(nums, target - nums[i])
            self.dp[target] = out

            return out


class SolutionDPMap:
    # Runtime: 32 ms, faster than 99.50% of Python3 online submissions.
    # Memory Usage: 14 MB, less than 48.19% of Python3 online submissions.
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.dp_map = {}
        self.dp_map[0] = 1
        return self.helper(nums, target)

    def helper(self, nums: List[int], target: int):
        if target <= 0:
            # 0 for all target < 0,
            # 1 for target = 0,
            return not target
        elif target in self.dp_map:
            return self.dp_map[target]
        else:
            out = 0
            for i in range(len(nums)):
                out += self.helper(nums, target - nums[i])
            self.dp_map[target] = out

            return out


if __name__ == "__main__":
    sol = SolutionDPMap()
    nums = [i for i in range(1, 10)]
    print(sol.combinationSum4(nums, target=10))
