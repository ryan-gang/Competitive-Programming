from collections import Counter


class Solution:
    # Runtime: 53 ms, faster than 60.18% of Python3 online submissions.
    # Memory Usage: 14 MB, less than 11.66% of Python3 online submissions.
    # Only works because input consists of only lowercase English chars.
    def checkIfPangram0(self, sentence: str) -> bool:
        return len(set(sentence)) == 26

    # Runtime: 49 ms, faster than 69.83% of Python3 online submissions.
    # Memory Usage: 13.9 MB, less than 11.66% of Python3 online submissions.
    # Only works because input consists of only lowercase English chars.
    def checkIfPangram1(self, sentence: str) -> bool:
        return len(Counter(sentence).keys()) == 26

    # Runtime: 70 ms, faster than 11.78% of Python3 online submissions.
    # Memory Usage: 13.9 MB, less than 54.73% of Python3 online submissions.
    def checkIfPangram2(self, sentence: str) -> bool:
        mask = int("1" * 26, 2)  # BETTER -> (1 << 26) - 1
        for char in sentence:
            char_idx = ord(char) - ord("a")
            bit_val = 1 << char_idx
            if mask & bit_val:
                mask ^= bit_val

        return mask == 0

    # Runtime: 80 ms, faster than 5.29% of Python3 online submissions.
    # Memory Usage: 13.9 MB, less than 11.66% of Python3 online submissions.
    def checkIfPangram3(self, sentence: str) -> bool:
        mask = 0
        for char in sentence:
            char_idx = ord(char) - ord("a")
            bit_val = 1 << char_idx
            mask |= bit_val

        return mask == int("1" * 26, 2)  # BETTER -> (1 << 26) - 1


if __name__ == "__main__":
    sol = Solution()
    assert sol.checkIfPangram3(sentence="thequickbrownfoxjumpsoverthelazydog")
    assert not sol.checkIfPangram3(sentence="leetcode")
