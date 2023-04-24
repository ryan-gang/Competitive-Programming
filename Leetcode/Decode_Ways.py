class Solution:
    # Runtime: 40 ms, faster than 79.39%.
    # Memory Usage: 13.9 MB, less than 80.45%.
    # T : O(N), S : O(N)
    def numDecodings(self, s: str) -> int:
        """
        dp[i] is the number of ways, we can decode the string upto ith index.
        For each index we have 2 choices,
        Either take ith element as solo, or take it as a duo.
        We check if both the scenarios are possible.
        If possible we increment the count of ways to decode.
        dp[i-2] is the number of ways, the string upto the i-2th index could be decoded.
        If ith index element can be taken as a double character, we add dp[i-2] to our dp[i]
        If ith index element can be taken as a single character, we add dp[i-1] to dp[i].
        Because dp[i-1] is the number of ways to decode the string upto i-1.
        Think of it as just adding this index element, to all those various ways.
        We just carry over that count. And wherever possible try to create a double char.
        But if ith index element is not valid, all the "ways" calculated upto dp[i-1]
        will be wasted. We do not carry forward that sum.
        """

        # There can and will be "0"s in the number, taken singly its not valid.
        # Taken doubly also it will create problems. So we need this list.
        allowed_values = [str(i) for i in range(1, 27)]
        allowed = set(allowed_values)
        # To make calculations on previous indices easier, and reduce edge cases.
        # Made dp of length s + 1.
        dp = [0 for _ in range(len(s) + 1)]
        # Very important, if this is not properly set, entire dp will be Zeroes.
        if s[0] in allowed:
            dp[0] = dp[1] = 1
        else:
            dp[0] = dp[1] = 0

        for i in range(1, len(s)):
            # The chars are calculated with "i" itself, but as dp is of length n + 1,
            # i here, corresponds to i + 1 in the dp array.
            single_char = s[i]
            double_char = s[i - 1 : i + 1]
            idx = i + 1
            if single_char in allowed:
                dp[idx] += dp[idx - 1]
            if double_char in allowed:
                dp[idx] += dp[idx - 2]
        return dp[-1]

    # T : O(N), S : O(N)
    def numDecodings1(self, s: str) -> int:
        """
        dp[i] -> total number of ways of decoding s upto index i.

        We iterate over each character, setting it as the end of our current
        string, and go backwards by length, (1 <= length < 3) we check if this
        string is valid or not, if it is valid we can have new decodings, where
        we just add this valid string to the decoded string upto start - 1.

        So, dp[end] += dp[start - 1]

        But, for the base case where we want to just have the first single
        character, we need dp[-1] for which we make dp of length n + 1, and set
        dp[0] = 1 which is the base case.
        """
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        for end in range(n):
            for length in range(0, 3):
                if end >= length:
                    start = end - length
                    if s[start] == "0":
                        continue
                    else:
                        num = int(s[start : end + 1])
                        if num > 0 and num <= 26:
                            dp[end + 1] += dp[start - 1 + 1]
        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    assert sol.numDecodings(s="12") == 2
    assert sol.numDecodings(s="226") == 3
    assert sol.numDecodings(s="06") == 0
    assert sol.numDecodings("11106") == 2
