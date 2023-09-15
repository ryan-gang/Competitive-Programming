class Solution:
    """
    Firstly we add all the words into a dict, along with their index. We will
    use this to generate the output array. Then, we generate all the possible
    prefixes and suffixes of each word. And check if any of them reversed is
    present in the dict or not. If it is present, then we check if the
    concatenation of the word and the prefix/suffix is a palindrome or not.
    Ex : BAT
        Prefixes : B, BA, BAT. Reversed : TAB, AB, B.
        Suffixes : T, AT, BAT. Reversed : TAB, TA, T.
    We can actually create palindromes using TAB, AB and TA.
    BATTAB, BATAB, TABAT.
    """

    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        def check_palindrome(s: str) -> bool:
            return s == s[::-1]

        d: dict[str, int] = {}
        for idx, val in enumerate(words):
            d[val] = idx
        res: list[list[int]] = []
        for idx, word in enumerate(words):
            n = len(word)
            for i in range(n + 1):
                suf = word[i:][::-1]
                pre = word[:i][::-1]
                if suf in d:
                    concat = suf + word
                    if check_palindrome(concat) and idx != d[suf]:
                        res.append([d[suf], idx])
                if i != n and pre in d:
                    # i!=n checks and removes cases where suf and pre give the
                    # same string ie the whole word. We handle that in the suf
                    # case and ignore the pre case.
                    concat = word + pre
                    if check_palindrome(concat) and idx != d[pre]:
                        res.append([idx, d[pre]])

        return res


if __name__ == "__main__":
    sol = Solution()
    assert sol.palindromePairs(words=["abcd", "dcba", "lls", "s", "sssll"]) == [
        [1, 0],
        [0, 1],
        [3, 2],
        [2, 4],
    ]
    assert sol.palindromePairs(words=["bat", "tab", "cat", "ac"]) == [[1, 0], [0, 1], [2, 3]]
    assert sol.palindromePairs(words=["a", ""]) == [[0, 1], [1, 0]]
    assert sol.palindromePairs(words=["a", "b", "c", "ab", "ac", "aa"]) == [
        [1, 3],
        [3, 0],
        [2, 4],
        [4, 0],
        [0, 5],
        [5, 0],
    ]
