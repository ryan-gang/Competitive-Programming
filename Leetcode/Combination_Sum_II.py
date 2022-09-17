from typing import List


class Solution:
    # Runtime: 127 ms, faster than 46.82% of Python3 online submissions.
    # Memory Usage: 13.9 MB, less than 93.24% of Python3 online submissions.
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.all: List[List[int]] = list()
        candidates.sort()
        self.candidates = candidates
        self.target = target
        self.combination([], 0, 0)
        return self.all

    def combination(self, currComb, currSum, currIndex) -> None:
        if currSum > self.target:
            return
        elif currSum == self.target:
            self.all.append(currComb[::])
            return
        else:
            for i in range(currIndex, len(self.candidates)):
                if i > currIndex and self.candidates[i - 1] == self.candidates[i]:
                    continue
                currCandidate = self.candidates[i]
                currComb.append(currCandidate)
                self.combination(
                    currComb,
                    currSum + currCandidate,
                    i + 1,
                )
                currComb.pop()


sol = Solution()
candidates, target = [10, 1, 2, 7, 6, 1, 5], 8
print(sol.combinationSum(candidates, target))
