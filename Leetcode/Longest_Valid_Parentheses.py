from collections import deque


class Solution:
    """
    First, we iterate over the string using a stack, and pop away all valid
    parentheses substrings. Finally if anything remains, its the indices of the
    parenthesis that make the string invalid. Then using the indices, we find
    the length of the various valid substrings, and return the largest one.
    Ref : 14126/my-o-n-solution-using-a-stack/
    """

    # T : O(N), S : O(N)
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        stack: deque[int] = deque()
        # Stack will finally hold the indices
        # that are not part of any valid substring.
        for idx, val in enumerate(s):
            if val == "(":
                stack.append(idx)
            else:
                if stack:
                    i = stack[-1]
                    if s[i] == "(":
                        stack.pop()
                    else:
                        stack.append(idx)
                else:
                    stack.append(idx)

        if not stack:
            return n

        a, b, max_length = n, 0, 0
        while stack:
            b = stack.pop()
            max_length = max(max_length, a - b - 1)
            a = b
        max_length = max(max_length, a)
        return max_length

    """
    longest[i] stores the longest length of a valid parentheses that ends at index i.
    If s[i] is '(', set longest[i] to 0, because any string that ends with '(' is not valid.
    Else if s[i] is ')'
         If s[i-1] is '(', longest[i] = longest[i-2] + 2
         Else if s[i-1] is ')' and s[i-longest[i-1]-1] == '(',
         longest[i] = longest[i-1] + 2 + longest[i-longest[i-1]-2]
    Which basically means if current is ")" and the previous char
    is also ")", we need to check if that is the ending of a valid
    susbtring. If it is, we just add that length to our current length.
    Ex : ((()) ")" ()
    """
    # T : O(N), S : O(N)
    def longestValidParentheses1(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        max_length = 0
        for i in range(1, n):
            if s[i] == ")":
                # case 1: ()()
                if s[i - 1] == "(":
                    # add nearest parentheses pairs + 2
                    dp[i] = dp[i - 2] + 2
                # case 2: (())
                # i-dp[i-1]-1 is the index of last "(" not paired until this ")"
                elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                    if dp[i - 1] > 0:  # content within current matching pair is valid
                        # add nearest parentheses pairs + 2 + parentheses before last "("
                        dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                    else:
                        # otherwise is 0
                        dp[i] = 0
                max_length = max(max_length, dp[i])

        return max_length


if __name__ == "__main__":
    sol = Solution()
    assert sol.longestValidParentheses(s="()((((())))(()(()(()(()(()(()") == 8
    assert sol.longestValidParentheses(s=")()())") == 4
    assert sol.longestValidParentheses(s="())") == 2
