import sys


# Runtime: 2506 ms, faster than 22.75%.
# Memory Usage: 22.7 MB, less than 42.11%.
# T : O(NLogN), S : O(N)
# Merge Sort.
class Solution:
    @staticmethod
    def divide(array: list[int]) -> tuple[list[int], list[int]]:
        N = len(array)
        return array[: N // 2], array[N // 2 :]

    @staticmethod
    def merge(first: list[int], second: list[int]) -> list[int]:
        out: list[int] = []
        i = j = 0
        while i < len(first) or j < len(second):
            if i < len(first):
                val1 = first[i]
            else:
                val1 = sys.maxsize
            if j < len(second):
                val2 = second[j]
            else:
                val2 = sys.maxsize

            if val1 < val2:
                out.append(val1)
                i += 1
            else:
                out.append(val2)
                j += 1

        return out

    def sortArray(self, array: list[int]) -> list[int]:
        first, second = Solution.divide(array)

        if len(first) > 1:
            first = self.sortArray(first)
        if len(second) > 1:
            second = self.sortArray(second)

        return Solution.merge(first, second)


if __name__ == "__main__":
    sol = Solution()
    print(sol.sortArray(array=[5, 6, 4, 3, 2, 0, 9, 1]))
    print(sol.sortArray(array=[5, 6]))
    print(sol.sortArray(array=[5]))
