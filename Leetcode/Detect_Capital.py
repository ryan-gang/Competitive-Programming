class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        f = lambda s: s.upper() == s
        g = lambda s: s.lower() == s
        h = lambda s: s[0].lower() + s[1:] == s.lower()

        return f(word) or g(word) or h(word)

    def detectCapitalUse1(self, word: str) -> bool:
        return len(word) == 1 or word[1:].islower() or word.isupper()

    def detectCapitalUse2(self, word):
        return word.isupper() or word.islower() or word.istitle()
