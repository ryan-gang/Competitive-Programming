from typing import List


# 51/79 TC passed.
# This method didn't work because in the dp array
# I am keeping track of (does ANY 4 letter word create a chain with another 5 letter word)
# and then using that value in the next word combination's chain.
# So this method thinks a valid chain is a -> ab -> abc / def -> defg -> defgh
# In this case output should be 3, but actually is 5.
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda item: len(item))

        dp = [1 for _ in range(len(words[-1]))]
        i, j, N = 0, 0, len(words)
        while i < N:
            j = i + 1
            while j < N:
                if len(words[j]) - len(words[i]) > 1:
                    break
                elif len(words[j]) - len(words[i]) < 1:
                    j += 1
                    continue
                else:
                    assert len(words[j]) - len(words[i]) == 1
                    status = self.check_for_string_chain(words[i], words[j])
                    if status:
                        dp[len(words[j]) - 1] = dp[len(words[i]) - 1] + 1
                j += 1
            i += 1
        return max(dp)

    def check_for_string_chain(self, wordA: str, wordB: str) -> bool:
        a, b, flag = 0, 0, 0
        while a < len(wordA) and b < len(wordB):
            if wordA[a] == wordB[b]:
                a += 1
                b += 1
            else:
                if not flag:
                    flag = True
                    b += 1  # wordB is the longer word.
                else:
                    return False
        return True


# words = ["a", "b", "ba", "bca", "bda", "bdca"]
# words = ["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]
# words = ["abcd", "dbqca"]

sol = Solution()
# Should be 7
print(
    sol.longestStrChain(
        words=[
            "ksqvsyq",
            "ks",
            "kss",
            "czvh",
            "zczpzvdhx",
            "zczpzvh",
            "zczpzvhx",
            "zcpzvh",
            "zczvh",
            "gr",
            "grukmj",
            "ksqvsq",
            "gruj",
            "kssq",
            "ksqsq",
            "grukkmj",
            "grukj",
            "zczpzfvdhx",
            "gru",
        ]
    )
)
