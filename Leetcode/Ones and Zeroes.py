from typing import List


# strs = ["10", "0001", "111001", "1", "0"]
# m = 5
# n = 3
# strs, m, n = ["10", "0", "1"], 1, 1
strs, m, n = ["001", "110", "0000", "0000"], 9, 2
strs = sorted(strs, key=lambda item: len(item))
out = 0


def countBits(binary):
    ones, zeros = 0, 0
    for digit in binary:
        if digit == "1":
            ones += 1
        else:
            zeros += 1
    return zeros, ones


M, N = 0, 0
for string in strs:
    z, o = countBits(string)
    M, N = M + z, N + o
    if M > m or N > n:
        M, N = M - z, N - z
    else:
        out += 1
        print(string)


class Solution:
    # 24/71 TC passed.
    def findMaxFormWrongBrute(self, strs: List[str], m: int, n: int) -> int:
        out = set()
        for _ in strs:
            z, o = self.countBits(_)
            if z <= m and o <= n:
                out.append(_)
        return len(out)

    def countBits(self, binary):
        ones, zeros = 0, 0
        for digit in binary:
            if digit == "1":
                ones += 1
            else:
                zeros += 1
        return zeros, ones

    # 57/71 TC passed.
    def findMaxFormGreedy(self, strs: List[str], m: int, n: int) -> int:
        out = 0
        strs = sorted(strs, key=lambda item: len(item))
        M, N = 0, 0
        for string in strs:
            z, o = self.countBits(string)
            M, N = M + z, N + o
            if M > m or N > n:
                M, N = M - z, N - z
            else:
                out += 1
        return out
