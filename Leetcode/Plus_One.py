class Solution:
    # T : O(N), S : O(1)
    def plusOne(self, digits: list[int]) -> list[int]:
        carry = 0
        digits[-1] += 1
        if digits[-1] > 9:
            carry = digits[-1] // 10
            digits[-1] %= 10
        i = len(digits) - 2
        while i >= 0:
            val = digits[i]
            if carry:
                val += carry
                carry = val // 10
                val %= 10
            digits[i] = val

            i -= 1

        if carry:
            digits = [carry] + digits

        print("".join(map(str, digits)))
        return digits

    def plusOneConcise(self, digits: list[int]) -> list[int]:
        # Instead of handling the addition of 1, just make carry as 1, and start
        # the process from the last digit.
        carry, i = 1, len(digits) - 1
        while i >= 0:
            val = digits[i]
            val += carry
            carry = val // 10
            val %= 10
            digits[i] = val

            i -= 1

        if carry:
            digits = [carry] + digits

        return digits


if __name__ == "__main__":
    sol = Solution()
    assert sol.plusOne(digits=[1, 2, 3]) == [1, 2, 4]
    assert sol.plusOne(digits=[9]) == [1, 0]
    assert sol.plusOne(digits=[2, 9, 9, 9]) == [3, 0, 0, 0]
