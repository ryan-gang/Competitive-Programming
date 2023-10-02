class Solution:
    # T : O(N), S : O(1)
    # For every contiguous substring that exceeds a length of 2, we can get
    # (length - 2) of valid moves for that player. So we just count substring
    # lengths.
    def winnerOfGame(self, colors: str) -> bool:
        colors = colors + "C"  # To handle the last character
        a, b = 0, 0  # Total valid moves for alice & bob
        length = 0
        for idx, val in enumerate(colors):
            prev = colors[idx - 1]
            if val != prev:
                if prev == "A":
                    a += max(0, length - 2)
                else:
                    b += max(0, length - 2)
                length = 1
            else:
                length += 1
        return a > b

    # Cleaner implementation.
    # T : O(N), S : O(1)
    def winnerOfGame1(self, colors: str) -> bool:
        alice = 0
        bob = 0

        for i in range(1, len(colors) - 1):
            if colors[i - 1] == colors[i] == colors[i + 1]:
                if colors[i] == "A":
                    alice += 1
                else:
                    bob += 1

        return alice - bob >= 1


if __name__ == "__main__":
    sol = Solution()
    assert sol.winnerOfGame(colors="AAABABB")
    assert not sol.winnerOfGame(colors="AA")
    assert not sol.winnerOfGame(colors="ABBBBBBBAAA")
    assert not sol.winnerOfGame(colors="AAB")
    assert not sol.winnerOfGame(colors="AAAABBBB")
