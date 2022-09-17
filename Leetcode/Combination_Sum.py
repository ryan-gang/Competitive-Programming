# from functools import lru_cache
from typing import List


class SolutionTLE:
    # 170/171 TC passed. TLE.
    # The difference between TLE and accepted solution is, this solution makes a function
    # call for *every* element in the candidates list. Disregarding what is already present
    # in the current sequence, the trick is to keep a track of the indices added to the
    # sequence and then not add them again.
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.all: List[List[int]] = list()
        self.candidates = candidates
        self.target = target
        self.helper([], 0)
        return self.all

    # @lru_cache(maxsize=None)
    # Cannot use lru_cache on a method, with a list as one of the inputs : "Unhashable type list"
    def helper(self, sequence: List[int], sum: int) -> None:
        if sum == self.target:
            sequence.sort()
            if sequence not in self.all:
                print(sequence)
                self.all.append(sequence)
        elif sum > self.target:
            return
        else:
            for i in self.candidates:
                self.helper(sequence + [i], sum + i)


class Solution:
    # Runtime: 123 ms, faster than 59.23% of Python3 online submissions.
    # Memory Usage: 14.1 MB, less than 72.86% of Python3 online submissions.
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.all: List[List[int]] = list()
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
            """Here starting the loop from currIndex, makes sure,
            we don't return permutations of the same sequence.
            Like [2,3,2], [2,2,3], [3,2,2]
            We only want anyone out of all these.
            But as new loop starts from currIndex and also currIndex is passed to next call,
            we will get repetitions, as requested."""
            for i in range(currIndex, len(self.candidates)):
                currCandidate = self.candidates[i]
                currComb.append(currCandidate)
                self.combination(
                    currComb,
                    currSum + currCandidate,
                    i,
                )
                currComb.pop()


sol = Solution()
candidates, target = [100, 200, 4, 12], 400
print(sol.combinationSum(candidates, target))
