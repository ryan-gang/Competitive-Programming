class Solution:
    # Runtime: 40 ms, faster than 79.39% of Python3 online submissions.
    # Memory Usage: 13.9 MB, less than 80.45% of Python3 online submissions.
    def numDecodings(self, s: str) -> int:
        allowed_values = [str(i) for i in range(1, 27)]
        allowed = set(allowed_values)

        # To make calculations on previous indices easier, and reduce edge cases.
        # Made dp of length s + 1.
        dp = [0 for _ in range(len(s) + 1)]

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
        if s[0] in allowed:
            dp[0] = dp[1] = 1
        else:
            dp[0] = dp[1] = 0

        for i in range(1, len(s)):
            single_char = s[i]
            double_char = s[i - 1: i + 1]
            idx = i + 1
            if single_char in allowed:
                dp[idx] += dp[idx - 1]
            if double_char in allowed:
                dp[idx] += dp[idx - 2]
        return dp[-1]


sol = Solution()
assert sol.numDecodings(s="12") == 2
assert sol.numDecodings(s="226") == 3
assert sol.numDecodings(s="06") == 0
assert sol.numDecodings("11106") == 2
