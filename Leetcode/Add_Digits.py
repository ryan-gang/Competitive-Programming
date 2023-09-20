class Solution:
    # T : O(NlogN), S : O(1)
    def addDigitsNaive(self, num: int) -> int:
        while len(str(num)) > 1:
            num = sum(int(i) for i in str(num))

        return num

    # T : O(NlogN), S : O(1)
    def addDigits(self, num: int) -> int:
        while num > 9:
            add = 0
            while num:
                add += num % 10
                num //= 10
            num = add
        return num

    # https://en.wikipedia.org/wiki/Digital_root
    def addDigits1(self, num: int) -> int:
        return 1 + (num - 1) % 9 if num else 0


if __name__ == "__main__":
    sol = Solution()
    assert (sol.addDigitsNaive(num=38)) == 2
    assert (sol.addDigitsNaive(num=0)) == 0
