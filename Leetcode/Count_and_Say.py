# Runtime: 221 ms, faster than 5.02% of Python3 online submissions.
# Memory Usage: 14 MB, less than 30.54% of Python3 online submissions.class Solution:
class Solution:
    def __init__(self) -> None:
        """As our higher limit is pretty small, we precompute the entire cache,
        and finally just return cache read values."""
        self.memo = {}
        for i in range(1, 31):
            self.memo[i] = self.say_n((i))

    @staticmethod
    def say(n: str) -> str:
        """Given any string 'n' return the 'said' version of the string."""
        out = ""
        count = 0
        prev = n[0]

        for num in n:
            if prev == num:
                count += 1
            else:
                out += f"{count}{prev}"
                count = 1
            prev = num

        out += f"{count}{prev}"
        return out

    def say_n(self, n: int) -> str:
        """Given an integer n, recursively finds the 'count_and_said' version of it from scratch.
        Where 'count_and_said'(n) = say(n-1)
        This method should be renamed to count_and_say"""
        if n < 2:
            return "1"
        if n not in self.memo:
            self.memo[n] = Solution.say(self.say_n(n - 1))
        return self.memo[n]

    def countAndSay(self, n: int) -> str:
        return self.memo[n]


if __name__ == "__main__":
    sol = Solution()
    assert sol.countAndSay(n=1) == "1"
    assert sol.countAndSay(n=4) == "1211"
