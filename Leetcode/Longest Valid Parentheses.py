from collections import deque


# 156/231 passed, fails for : s = "()(()"
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        reverse = {")": "("}
        stack = deque()
        count, maxCount = 0, 0

        for i in s:
            if i not in reverse:
                stack.append(i)
            else:
                if stack and stack[-1] == reverse[i]:
                    stack.pop()
                    count += 2
                    maxCount = max(count, maxCount)
                else:
                    stack = deque()
                    count = 0
        return maxCount
