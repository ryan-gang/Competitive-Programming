from collections import deque


class Solution:
    def addBinaryNaive(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2)).split("b")[1]

    # Time : 71 ms 5%, Space : 22.5%
    def addBinary(self, a: str, b: str) -> str:
        # Pad the smaller number with zeroes to the left, make both strings equal in length.
        if len(a) < len(b):
            padding = (len(b) - len(a)) * "0"
            a = padding + a
        else:
            padding = (len(a) - len(b)) * "0"
            b = padding + b

        out: list[str] = []
        carry = 0
        for i, j in zip(a[::-1], b[::-1]):
            val = int(i) + int(j) + carry
            if val > 1:
                carry = 1
                val %= 2
            else:
                carry = 0
            out.append(str(val))
        if carry == 1:
            out.append(str(carry))

        return "".join(out[::-1])

    def addBinary1(self, a: str, b: str) -> str:
        res: deque[str] = deque()

        add = carry = 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0:
            if i >= 0:
                p = a[i]
            else:
                p = 0
            if j >= 0:
                q = b[j]
            else:
                q = 0
            add = carry
            carry = 0
            if p == "1":
                add += 1
            if q == "1":
                add += 1
            if add > 1:
                n_add = add % 2
                carry = add // 2
                add = n_add
            res.appendleft(str(add))
            i -= 1
            j -= 1
        if carry:
            res.appendleft(str(carry))
        out = "".join(res)
        return out

    # T : O(N), S : O(N)
    # Where N is length of longer string.
    def addBinary2(self, a: str, b: str) -> str:
        i, j, carry = len(a) - 1, len(b) - 1, 0
        out: deque[str] = deque()
        while i >= 0 or j >= 0:
            add = carry
            if i >= 0:
                add += ord(a[i]) - ord("0")
            if j >= 0:
                add += ord(b[j]) - ord("0")
            carry = add // 2
            add = add % 2
            out.appendleft(str(add))
            i -= 1
            j -= 1

        if carry > 0:
            out.appendleft(str(carry))

        return "".join(out)


if __name__ == "__main__":
    sol = Solution()
    assert sol.addBinary(a="1010", b="1011") == "10101"
    assert sol.addBinary(a="11", b="1") == "100"
    assert sol.addBinary(a="1111", b="1111") == "11110"
    assert sol.addBinary(a="111111", b="111111111") == "1000111110"
