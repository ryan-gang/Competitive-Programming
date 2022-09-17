from typing import Dict, List


class Solution:
    # Runtime: 34 ms, faster than 92.91% of Python3 online submissions.
    # Memory Usage: 13.8 MB, less than 76.64% of Python3 online submissions.
    # T : O(N), S : O(1)
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        out = []
        for word in words:
            if self.match_pattern(word=word, pattern=pattern):
                out.append(word)

        return out

    def match_pattern(self, word: str, pattern: str) -> bool:
        """
        Creating the pattern to word mapping for each letter,
        if there are any inconsistencies return False.
        Each character in pattern, should map to the same character in word.
        If a different character in pattern maps to the same character in word, return False.
        Same thing can also be done with 2 dictionaries, easier code, but more space required. (?)
        """
        index = 0
        pattern2word: Dict[str, str] = {}
        seen_chars = set()
        while index < len(word):
            char = word[index]
            pattern_char = pattern[index]
            if pattern_char in pattern2word:
                # if pattern character is seen before,
                # assert that pattern2word mapping matches with the current word character.
                if not pattern2word[pattern_char] == char:
                    return False
            else:
                # If pattern character not seen before,
                # make sure the word character is also not seen before,
                # else there is an inconsistency, return False.
                if char in seen_chars:
                    return False
                # else add to dict, and set.
                pattern2word[pattern_char] = char
                seen_chars.add(char)
            index += 1

        return True

    def match(self, word: str, pattern: str):
        m1: Dict[str, str] = {}
        m2: Dict[str, str] = {}
        for w, p in zip(word, pattern):
            if w not in m1:
                m1[w] = p
            if p not in m2:
                m2[p] = w
            if (m1[w], m2[p]) != (p, w):
                return False
        return True


sol = Solution()
print(sol.findAndReplacePattern(words=["abc", "deq", "mee", "aqq", "dkd", "ccc"], pattern="abb"))
