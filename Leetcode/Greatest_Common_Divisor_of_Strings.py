from math import gcd


class Solution:
    # Runtime: 31 ms, faster than 86.37%.
    # Memory Usage: 13.8 MB, less than 70.81%.
    # T : O(min(M, N) x (M + N)), S : O(min(M, N))
    # min(M, N) number of prefixes, and we match if it can be multiplied to get str1 and str2,
    # which is (M + N).
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Instead of going from small to large, we should go from large to small.
        # Will save a lot of iterations. Return at the first chance.
        n1, n2 = len(str1), len(str2)
        n = min(n1, n2)
        str = min(str1, str2)
        div = ""

        for i in range(n):
            prefix = str[: i + 1]
            length = i + 1
            k1 = n1 // length
            k2 = n2 // length
            if (
                n1 % length == 0
                and n2 % length == 0
                and prefix * k1 == str1
                and prefix * k2 == str2
            ):
                div = prefix

        return div

    def gcdOfStrings1(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        def valid(k: int) -> bool:
            if len1 % k or len2 % k:
                return False
            n1, n2 = len1 // k, len2 // k
            base = str1[:k]
            return str1 == n1 * base and str2 == n2 * base

        for i in range(min(len1, len2), 0, -1):
            if valid(i):
                return str1[:i]
        return ""

    # T : O(M + N), S : O(M + N)
    def gcdOfStrings2(self, str1: str, str2: str) -> str:
        """
        If str1 = mX and str2 = nX, str1 + str2 = str2 + str1 = (m + n)X.
        If str1 = mX and str2 = nY, str1 + str2 = mX + nY, str2 + str1 = nY + mX.
        This way we can verify if `divisible strings` are present.
        And the length has to be gcd(str1, str2).
        str1 = mX, str2 = nX, longest common string is X, which is again the GCD of str1 and str2.
        Ref : https://leetcode.com/problems/greatest-common-divisor-of-strings/
        solutions/3024822/greatest-common-divisor-of-strings/
        """
        # Check if they have non-zero GCD string.
        if str1 + str2 != str2 + str1:
            return ""

        # Get the GCD of the two lengths.
        max_length = gcd(len(str1), len(str2))
        return str1[:max_length]


if __name__ == "__main__":
    sol = Solution()
    assert sol.gcdOfStrings(str1="ABABAB", str2="ABAB") == "AB"
