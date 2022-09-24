from collections import deque

"""
Q. Given a string s representing characters typed into an editor, with "<-"
representing a backspace, return the current state of the editor.
A. As the backspace is 2 chars long, we will keep a window of the next 2 chars. If it is "<-" we
pop one element from the stack and take the window 2 places ahead (<-), else we take the window
one place ahead. We always append the first element of the window to the stack, so the "<" of the
"<-" is never added, and always skipped.
"""


class Solution:
    def solve(self, s):
        stack = deque()
        lo, hi = 0, 2
        window = s[lo:hi]
        while len(window) == 2:
            if window == "<-":
                if stack:
                    stack.pop()
                lo += 2
                hi += 2
            else:
                stack.append(window[0])
                lo += 1
                hi += 1
            window = s[lo:hi]
        stack.extend(window)
        return "".join(stack)


sol = Solution()
assert sol.solve(s="<") == "<"
assert sol.solve(s="abc<-z") == "abz"
assert sol.solve(s="<-x<-z<-") == ""
