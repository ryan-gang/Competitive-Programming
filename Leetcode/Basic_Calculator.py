from collections import deque


class Solution:
    # Runtime: 633 ms, faster than 5.05%.
    # Memory Usage: 15.6 MB, less than 37.31%.
    def calculate(self, s: str) -> int:
        val = 0
        sign = +1
        i = 0
        n = len(s)

        OPERATORS = {"+": 1, "-": -1}
        stack = deque()

        while i < n:
            char = s[i]
            if char in OPERATORS:
                sign = OPERATORS[char]
            if char == "(":
                stack.append(val)
                stack.append(sign)
                val = 0
                sign = +1
            if char == ")":
                print(stack)
                val = val * stack.pop() + stack.pop()
            elif char.isdigit():
                start = i
                while i < n and s[i].isdigit():
                    i += 1
                val += sign * int(s[start:i])
                continue
            i += 1
        return val


# Ref : discuss/1456850/Python-Basic-Calculator-I-II-III-easy-solution-detailed-explanation
# ToDo : BC - II, BC - III
if __name__ == "__main__":
    sol = Solution()
    for s in [
        "(1+(4+5+2)-3)+(6+8)",
        "1+4+5+2-3+6+8-10",
        "(1-(4+5-(1+12+3-14-(-12)    )+2)-3)+(6+8)",
        "(14-(-12))",
    ]:
        assert sol.calculate(s) == eval(s)
