import math


class Solution:
    # Runtime: 57 ms, faster than 22.63% of Python3 online submissions for Poor Pigs.
    # Memory Usage: 14 MB, less than 20.44% of Python3 online submissions for Poor Pigs.
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        rounds = math.floor(minutesToTest / minutesToDie)
        return math.ceil(math.log(buckets) / math.log(rounds + 1))


sol = Solution()
assert 5 == sol.poorPigs(1000, 15, 60)
assert 2 == sol.poorPigs(4, 15, 15)
assert 2 == sol.poorPigs(4, 15, 30)
