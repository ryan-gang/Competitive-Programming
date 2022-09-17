from collections import Counter

s = "abcabc"


class Solution:
    def minDeletions(self, s: str) -> int:
        d = Counter(s)
        v = sorted(list(d.values()))
        if len(set(v)) == len(v):
            return 0

        index, globalCount = 0, 0
        while index < len(v) - 1:
            val = v[index]
            if v[index + 1] == val:
                while val in v:
                    val -= 1
                    globalCount += 1

            index += 1

        return globalCount


d = Counter(s)
v = sorted(list(d.values()))
if len(set(v)) == len(v):
    print(0)

index, globalCount = 0, 0
while index < len(v) - 1:
    print("?")
    val = v[index]
    if v[index + 1] == val:
        while val in v:
            val -= 1
            print("Reduced")
            globalCount += 1
    print(index, val)
        # v[index] = val
    index += 1

print(globalCount)

