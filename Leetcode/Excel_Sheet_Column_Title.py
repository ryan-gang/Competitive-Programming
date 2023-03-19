from string import ascii_uppercase


class Solution:
    """
    In a 26-nary system.
    0 -> A
    25 -> Z
    26 -> AA
    However, in excel and for purposes of this question.
    1 -> A
    26 -> Z
    27 -> AA
    For a string "ABZ" it's corresponding columnNumber will be :
    n = (A+1) * 26^2 + (B+1) * 26^1 + (Z+1) * 26^0 ; where ABZ are from our 26-nary system.
                                                    So we add 1, to convert to excel's format.
    => n-1 = (A+1) * 26^2 + (B+1) * 26^1 + Z
    => (n-1) % 26 = Z                                    --- 1
    => (n-1) / 26 = (A+1) * 26^1 + (B+1) * 26^0          --- 2

    This is why, for every iteration we use 1 to obtain the current char.
    And 2 to prepare for the next iteration.
    """

    # Runtime: 31 ms, faster than 62.31%.
    # Memory Usage: 13.9 MB, less than 45.8%.
    # T : O(LogN), S : O(LogN) ;
    # Log 26 (N), is the number of iterations the loop will run for. (The max
    # exponent of 26 in n). We will also store this many digits in our output array.
    def convertToTitle(self, n: int) -> str:
        out: list[str] = []

        mapping: dict[int, str] = {}
        for c in ascii_uppercase:
            val = (ord(c) - ord("A")) + 1
            mapping[val] = c

        while n > 0:
            n -= 1
            char: int = (n) % 26
            out.append(mapping[char + 1])
            n //= 26
        return "".join(out[::-1])


if __name__ == "__main__":
    sol = Solution()
    assert sol.convertToTitle(n=779) == "ACY"
    assert sol.convertToTitle(n=27) == "AA"
    assert sol.convertToTitle(n=701) == "ZY"
