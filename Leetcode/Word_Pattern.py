from collections import defaultdict


class Solution:
    # Runtime: 40 ms, faster than 63.75%.
    # Memory Usage: 13.8 MB, less than 74.33%.
    # T : O(N), S : O(N)
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        mapping = defaultdict(str)
        reverse = defaultdict(str)
        for char, word in zip(list(pattern), words):
            if char not in mapping and word not in reverse:
                mapping[char] = word
                reverse[word] = char
            else:
                if mapping[char] != word or reverse[word] != char:
                    return False
        return True

    def wordPattern0(self, p: str, s: str) -> bool:
        words, w_to_p = s.split(" "), dict()

        if len(p) != len(words):
            return False
        if len(set(p)) != len(set(words)):
            return False  # for the case w = ['dog', 'cat'] and p = 'aa'
            # No need for the 2nd dict, this removes all those cases.
        for i in range(len(words)):
            if words[i] not in w_to_p:
                w_to_p[words[i]] = p[i]
            elif w_to_p[words[i]] != p[i]:
                return False

        return True

    # All from StefanPochmann.
    def wordPattern1(self, pattern, str):
        s = pattern
        t = str.split()
        return map(s.find, s) == map(t.index, t)

    def wordPattern2(self, pattern, str):
        f = lambda s: map({}.setdefault, s, range(len(s)))
        return f(pattern) == f(str.split())

    def wordPattern3(self, pattern, str):
        s = pattern
        t = str.split()
        return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)


if __name__ == "__main__":
    sol = Solution()
    assert sol.wordPattern0("abba", "dog cat cat dog")
    assert not sol.wordPattern0("abba", "dog cat cat fish")
    assert not sol.wordPattern0("aaaa", "dog cat cat dog")
    assert not sol.wordPattern0("abba", "dog dog dog dog")
    assert not sol.wordPattern0("aaa", "dog dog dog dog")
