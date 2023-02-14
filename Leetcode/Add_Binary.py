from collections import deque


class Solution:
    def addBinary1(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2)).split("b")[1]

    # Runtime: 39 ms, faster than 48.9%.
    # Memory Usage: 13.9 MB, less than 18.5%.
    # T : O(N), S : O(N)
    def addBinary(self, a: str, b: str) -> str:
        out: deque[str] = deque()
        i, j, carry = len(a) - 1, len(b) - 1, 0

        while i >= 0 or j >= 0:
            add = carry
            # if i >= 0 and a[i] != "0":
            #     add += 1
            # if j >= 0 and b[j] != "0":
            #     add += 1
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
    assert sol.addBinary(a="11", b="1") == 100
    assert sol.addBinary(a="1010", b="1011") == 10101
