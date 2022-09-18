from collections import Counter, defaultdict


class Solution:
    # 41 / 43 TC passed. Wrong answer.
    # Order of chars not taken into consideration.
    # Broken by : "bbbaaaba", "aaabbbba"
    def isIsomorphicBroken(self, s: str, t: str) -> bool:
        ds = Counter(s)
        dt = Counter(t)

        return list(ds.values()) == list(dt.values())

    # Runtime: 40 ms, faster than 95.41% of Python3 online submissions.
    # Memory Usage: 14.3 MB, less than 45.95% of Python3 online submissions.
    def isIsomorphicAC(self, s: str, t: str) -> bool:
        mapping = {}  # Mapping of s -> t
        seen = set()  # Set of used chars in "t" ; because we don't want to reuse a mapped char.
        n = len(s)
        for _ in range(n):
            a, b = s[_], t[_]
            if a not in mapping:
                if b not in seen:
                    mapping[a] = b
                    seen.add(b)
                else:
                    return False
            else:
                if b != mapping[a]:
                    return False

        return True

    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_s_t, mapping_t_s = {}, {}
        for c1, c2 in zip(s, t):
            if (c1 not in mapping_s_t) and (c2 not in mapping_t_s):
                mapping_s_t[c1] = c2
                mapping_t_s[c2] = c1

            elif mapping_s_t.get(c1) != c2 or mapping_t_s.get(c2) != c1:
                return False

        return True

    def isIsomorphic1Liner(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))


class SolutionALL(object):
    def isIsomorphic(self, s, t):
        s2t, t2s = {}, {}
        for i in range(len(s)):
            if s[i] in s2t and s2t[s[i]] != t[i]:
                return False
            if t[i] in t2s and t2s[t[i]] != s[i]:
                return False
            s2t[s[i]] = t[i]
            t2s[t[i]] = s[i]
        return True

    def isIsomorphic1(self, s, t):
        d1, d2 = {}, {}
        for i, val in enumerate(s):
            d1[val] = d1.get(val, []) + [i]
        for i, val in enumerate(t):
            d2[val] = d2.get(val, []) + [i]
        return sorted(d1.values()) == sorted(d2.values())

    def isIsomorphic2(self, s, t):
        d1, d2 = [[] for _ in range(256)], [[] for _ in range(256)]
        for i, val in enumerate(s):
            d1[ord(val)].append(i)
        for i, val in enumerate(t):
            d2[ord(val)].append(i)
        return sorted(d1) == sorted(d2)

    def isIsomorphic3(self, s, t):
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))

    def isIsomorphic4(self, s, t):
        return [s.find(i) for i in s] == [t.find(j) for j in t]

    # Very important.
    # Encodes the strings into arrays of numbers, where each number is the position
    # where the character was first seen. Use of map is also interesting.
    # Another encoding method is present below, line 116.
    def isIsomorphic5(self, s, t):
        return map(s.find, s) == map(t.find, t)

    def isIsomorphic6(self, s, t):
        d1, d2 = [0 for _ in range(256)], [0 for _ in range(256)]
        for i in range(len(s)):
            if d1[ord(s[i])] != d2[ord(t[i])]:
                return False
            d1[ord(s[i])] = i + 1
            d2[ord(t[i])] = i + 1
        return True


sol = Solution()
assert sol.isIsomorphic(s="egg", t="add")
assert sol.isIsomorphic(s="paper", t="title")
assert not sol.isIsomorphic(s="foo", t="bar")
assert not sol.isIsomorphic(s="bbbaaaba", t="aaabbbba")
assert not sol.isIsomorphic("badc", "baba")

####################################################################################################
"""
FOLLOW UP :
Group the isomorphic strings.
input = ['aab', 'xxy', 'xyz', 'abc', 'def', 'xyx']

return = [["xyx"], ["xyz", "abc", "def"], ["aab", "xxy"]]
We can "encode" the isomorphic strings and then based on
that encoding, add it into a dictionary.
"""


def groupIsomorphic(strs):
    # Encoding is character -> the index of the character in a set.
    def encode(s):
        d = {}
        encoded = []
        for c in s:
            if c not in d:
                d[c] = len(d)
            encoded.append(d[c])
        return str(encoded)

    groups = {}
    for s in strs:
        encoded = encode(s)
        if encoded not in groups:
            groups[encoded] = []
        groups[encoded].append(s)

    return list(groups.values())


print(groupIsomorphic(["aab", "xxy", "xyz", "abc", "def", "xyx"]))


# MUCH SHORTER ->
def groupIsomorphic(strs):
    mapping = defaultdict(list)
    for s in strs:
        key = tuple([s.find(i) for i in s])  # Encoding.
        mapping[key].append(s)
    return list(mapping.values())
