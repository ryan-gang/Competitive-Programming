from StarterCode.disjoint_set_union import Union

# Needlessly complicated helper method. Might have been useful if the strings
# were actually different. But as it is given that the strings are anagrams, we
# can just keep a count and return.
# Changing this method, the submission went from 5th percentile to 95th percentile.
# def check_for_similarity(str1: str, str2: str) -> bool:
#     i = diff = 0
#     changed: list[int] = []
#     while i < len(str1):
#         if str1[i] != str2[i]:
#             diff += 1
#             changed.append(i)
#         i += 1

#     return (
#         (diff == 2)
#         and (str1[changed[0]] == str2[changed[1]])
#         and (str1[changed[1]] == str2[changed[0]])
#     ) or (diff == 0)


class Solution:
    @staticmethod
    def check_for_similarity(str1: str, str2: str) -> bool:
        changes = 0
        for i, j in zip(str1, str2):
            if i != j:
                if changes == 2:
                    return False
                changes += 1

        return changes == 2 or changes == 0

    # Runtime: 253 ms, faster than 82.29%.
    # Memory Usage: 16.8 MB, less than 10.16%.
    # T : O(N^2 * M), S : O(N) ; Amortized UF ops are ~ O(1).
    def numSimilarGroups(self, strs: list[str]) -> int:
        n = len(strs)
        uf = Union(n)
        for i in range(n):
            uf.new(i)

        for i in range(n):
            for j in range(i + 1, n):
                str1, str2 = strs[i], strs[j]
                if Solution.check_for_similarity(str1, str2):
                    print(str1, str2)
                    uf.union(i, j)

        components = 0
        seen: set[int] = set()
        for i in range(n):
            if uf.find(i) not in seen:
                seen.add(uf.find(i))
                components += 1

        return components


if __name__ == "__main__":
    sol = Solution()
    assert sol.numSimilarGroups(strs=["tars", "rats", "arts", "star"]) == 2
    assert sol.numSimilarGroups(strs=["abc", "abc"]) == 1
