import collections
from typing import List


# 4/13 passed. TLE.
class WordFilter:
    prefix = collections.defaultdict(set)
    suffix = collections.defaultdict(set)
    words = []

    def __init__(self, words: List[str]):
        WordFilter.words = words
        for i, word in enumerate(words):
            length = 0
            while length <= len(word):
                pre = word[:length]
                suf = word[length:]
                self.prefix[pre].add(i)
                self.suffix[suf].add(i)
                length += 1

    def f(self, pre: str, suf: str) -> int:
        pre_words = set(self.prefix[pre])
        suf_words = set(self.suffix[suf])
        all_words = list(pre_words.intersection(suf_words))

        if len(all_words) == 0:
            return -1
        elif len(all_words) == 1:
            return all_words[0]
        else:
            return sorted(all_words, key=lambda item: len(self.words[item]), reverse=False)[-1]


# # Your WordFilter object will be instantiated and called as such:
obj = WordFilter(words=["apple"])
print(obj.f(pre="a", suf="e"))

# WRONG ANSWER TODO
# 2164886 Python faster than 96 No Trie
