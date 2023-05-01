from sys import maxsize


class Solution:
    def average(self, salary: list[int]) -> float:
        add = 0
        small = maxsize
        large = 0
        n = len(salary)
        for val in salary:
            small = min(small, val)
            large = max(large, val)
            add += val

        return (add - (small + large)) / (n - 2)


if __name__ == "__main__":
    sol = Solution()
    assert sol.average(salary=[4000, 3000, 1000, 2000]) == 2500.00000
