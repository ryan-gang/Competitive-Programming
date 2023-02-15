from collections import deque


class Solution:
    # Runtime: 291 ms, faster than 87.19%.
    # Memory Usage: 15.2 MB, less than 36.53%.
    # T : O(N), S : O(N)
    def addToArrayForm(self, num: list[int], K: int) -> deque[int]:
        k: list[int] = [int(i) for i in str(K)]
        out: deque[int] = deque()
        i, j = len(num) - 1, len(k) - 1
        carry = 0
        while i >= 0 or j >= 0:
            add = carry
            if i >= 0:
                add += num[i]
            if j >= 0:
                add += k[j]

            carry = add // 10
            add %= 10
            i -= 1
            j -= 1
            out.appendleft(add)

        if carry > 0:
            out.appendleft(carry)

        return out


if __name__ == "__main__":
    sol = Solution()
    assert sol.addToArrayForm(num=[1, 2, 0, 0], K=34) == [1, 2, 3, 4]
    assert sol.addToArrayForm(num=[2, 7, 4], K=181) == [4, 5, 5]
    assert sol.addToArrayForm(num=[2, 1, 5], K=806) == [1, 0, 2, 1]
