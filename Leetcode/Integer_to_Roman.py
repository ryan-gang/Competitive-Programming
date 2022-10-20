class Solution:
    # Runtime: 111 ms, faster than 28.07% of Python3 online submissions.
    # Memory Usage: 13.9 MB, less than 80.12% of Python3 online submissions.
    """
    From larger to smaller roman numeral, see if our n is greater than the numeral or not,
    if greater than calculate how many times it's greater,
    then add that many times of the numeral to the output."""

    def intToRoman(self, n: int) -> str:
        d = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }

        out = ""
        for integer in d:
            out += n // integer * d[integer]
            n %= integer

        return out


class Solution2:
    """Initial solution by me. A bit complicated."""

    mapping = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M",
    }

    def intToRoman(self, n: int) -> str:
        romans = sorted(list(Solution2.mapping.keys()), reverse=True)
        notation = []
        while n >= 0:
            i = 0
            while i < (len(romans)):
                num = romans[i]
                diff = n - num
                if diff >= 0:
                    notation.append(Solution2.mapping[num])
                    n = diff
                    i = -1
                i += 1

            if n == 0:
                break
        return "".join(notation)


if __name__ == "__main__":
    sol = Solution()
    assert sol.intToRoman(3) == "III"
    assert sol.intToRoman(58) == "LVIII"
    assert sol.intToRoman(20) == "XX"
    assert sol.intToRoman(1994) == "MCMXCIV"
