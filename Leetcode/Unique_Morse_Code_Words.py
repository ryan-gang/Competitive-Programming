from collections import defaultdict
from typing import List


class Solution:
    morse = [
        ".-",
        "-...",
        "-.-.",
        "-..",
        ".",
        "..-.",
        "--.",
        "....",
        "..",
        ".---",
        "-.-",
        ".-..",
        "--",
        "-.",
        "---",
        ".--.",
        "--.-",
        ".-.",
        "...",
        "-",
        "..-",
        "...-",
        ".--",
        "-..-",
        "-.--",
        "--..",
    ]

    def get_morse_code_from_string(self, s: str) -> str:
        code = ""
        for i in s:
            idx = ord(i) - ord("a")
            code += Solution.morse[idx]
        return code

    # Runtime: 53 ms, faster than 56.84% of Python3 online submissions.
    # Memory Usage: 13.9 MB, less than 75.48% of Python3 online submissions.
    # T : O(N), S : O(N)
    # for loop in get_morse_code will only run for 12 iterations at most.
    # 12 is the max length of a word. So T : O(12 * N)
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = defaultdict(int)

        for word in words:
            code = self.get_morse_code_from_string(word)
            codes[code] += 1

        return len(codes.keys())

    def uniqueMorseRepresentationsSol(self, words):
        MORSE = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]

        seen = {"".join(MORSE[ord(c) - ord("a")] for c in word) for word in words}

        return len(seen)


sol = Solution()

assert sol.uniqueMorseRepresentations(words=["gin", "zen", "gig", "msg"]) == 2
assert sol.uniqueMorseRepresentations(words=["a"]) == 1
