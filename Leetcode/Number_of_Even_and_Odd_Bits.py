class Solution:
    # T : O(LogN), S : O(1)
    # Log N iterations over binary N.
    def evenOddBit(self, n: int) -> list[int]:
        # Standard solution.
        binary = str(bin(n)).split("b")[1][::-1]

        even = odd = 0
        for i in range(len(binary)):
            if binary[i] == "1":
                if not i % 2:
                    even += 1
                else:
                    odd += 1

        return [even, odd]

    def evenOddBit1(self, n: int) -> list[int]:
        # Masks the odd and even places and returns the corresponding bit counts.
        return [(n & int("0101010101", 2)).bit_count(), (n & int("1010101010", 2)).bit_count()]


if __name__ == "__main__":
    sol = Solution()
    assert sol.evenOddBit(n=17) == [2, 0]
    assert sol.evenOddBit(n=2) == [0, 1]
