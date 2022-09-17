from typing import List


class SolutionL:
    # 45 / 59 TC passed. Wrong Answer.
    # There can be a situation, where words[i-1] is not the previous entry in the expected sequence.
    # We currently have no way of finding that entry out.
    # Ex sequence -> words = ["o", "on", "onpd", "onpdu", "ot", "oti", "otif"]
    # "ot" should be preceded by "o", as per our expectation.
    def longestWordWrong(self, words: List[str]) -> str:
        n = len(words)
        words.sort()
        # Sequence has to start from length = 1
        # As long as sequence is increasing, and each word is "related" we're good.
        # If length is same, sequence is broken.
        longest = ""
        sequence_started_flag = len(words[0]) == 1
        for i in range(1, n):
            curr = words[i]
            prev = words[i - 1]
            if sequence_started_flag and curr[:-1] == prev:
                # We are good. Length and content both are checked.
                if len(curr) > len(longest):
                    longest = curr
            else:
                # Sequence broken.
                # Now unless we see a single letter word, new sequence will not start.
                sequence_started_flag = False
            if not sequence_started_flag and len(curr) == 1:
                sequence_started_flag = True

        return longest

    # 48 / 59 TC passed. Wrong Answer.
    # Possibly issues with sequence starts, after a different word cuts in between.
    def longestWordWrong2(self, words: List[str]) -> str:
        n = len(words)
        words.sort()
        words_set = set()
        # Sequence has to start from length = 1
        # As long as sequence is increasing, and each word is "related" we're good.
        # If length is same, sequence is broken.
        longest = words[0]
        sequence_started_flag = len(words[0]) == 1
        for i in range(1, n):
            curr = words[i]
            prev = words[i - 1]
            words_set.add(prev)
            sequence_started_flag = sequence_started_flag or len(curr) <= 2
            if sequence_started_flag and curr[:-1] in words_set:
                # We are good. Length and content both are checked.
                if len(curr) > len(longest):
                    longest = curr
            else:
                # Sequence broken.
                # Now unless we see a single letter word, new sequence will not start.
                sequence_started_flag = False
            if not sequence_started_flag and len(curr) == 1:
                sequence_started_flag = True

        return longest


# Create all prefixes of words, check if all prefixes in set.
# Return longest such word.
class Solution:
    # Runtime: 114 ms, faster than 87.00% of Python3 online submissions.
    # Memory Usage: 14.3 MB, less than 91.98% of Python3 online submissions.
    def longestWord(self, words: List[str]) -> str:
        # Sort words, first by decreasing length.
        # If ties, then sort lexicographically.
        words.sort(key=lambda c: (-len(c), c))
        words_set = set(words)
        for word in words:
            # All prefixes of word has to be in set.
            condition = True
            for i in range(1, len(word)):
                condition = condition and (word[:-i] in words_set)
            if condition:
                return word
            # Much concise representation :
            # if all(word[:-i] in words_set for i in range(1, len(word))):
            #     return word

        return ""


sol = Solution()
print(sol.longestWord(words=["a", "banana", "app", "appl", "ap", "apply", "apple"]))
assert sol.longestWord(words=["w", "wo", "wor", "worl", "world"]) == "world"
assert sol.longestWord(words=["a", "banana", "app", "appl", "ap", "apply", "apple"]) == "apple"
assert (
    sol.longestWord(
        words=[
            "rac",
            "rs",
            "ra",
            "on",
            "r",
            "otif",
            "o",
            "onpdu",
            "rsf",
            "rs",
            "ot",
            "oti",
            "racy",
            "onpd",
        ]
    )
    == "otif"
)
