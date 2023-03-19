from string import ascii_uppercase


class Solution:
    # Runtime: 40 ms, faster than 28.91%.
    # Memory Usage: 13.8 MB, less than 46.4%.
    # T : O(N), S : O(1), where N is len(columnTitle)
    def titleToNumber(self, columnTitle: str) -> int:
        # We are basically converting a number from base 26 system to decimal.
        mapping = {}
        for char in ascii_uppercase:
            val = ord(char) - ord("A") + 1
            mapping[char] = val

        exponent = 0
        column: int = 0
        for i in range(len(columnTitle) - 1, -1, -1):
            column += mapping[columnTitle[i]] * (26**exponent)
            exponent += 1

        return column


if __name__ == "__main__":
    sol = Solution()
    assert sol.titleToNumber("AB") == 28
    assert sol.titleToNumber("A") == 1
    assert sol.titleToNumber("ZY") == 701
