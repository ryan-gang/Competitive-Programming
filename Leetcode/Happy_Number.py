class Solution:
    # Runtime: 74 ms, faster than 11.71% of Python3 online submissions.
    # Memory Usage: 14 MB, less than 15.19% of Python3 online submissions.
    def __init__(self) -> None:
        self.happy_nums = set([1])

    def isHappy(self, n: int) -> bool:
        nums = set()
        while n != 1:
            if n in nums:
                return False
            elif n in self.happy_nums:
                return True
            nums.add(n)
            n = self.find_digit_squares(n)
        self.happy_nums.update(nums)
        return True

    def find_digit_squares(self, n: int):
        squared = 0
        while n:
            digit = n % 10
            n = int(n / 10)
            squared += pow(digit, 2)
        return squared


sol = Solution()
assert not (sol.isHappy(n=2))
assert sol.isHappy(n=19)
assert sol.isHappy(n=7)
print(sol.happy_nums)
