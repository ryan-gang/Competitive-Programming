class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        """
        1. Check if a proper swap is possible. (Mismatching chars, and their proper positions.)
        2. Check if the words are actually same, then in
        that case repeated letters are present or not.
        (Which can be swapped)
        """
        repeated = False
        seen_s: set[str] = set()
        seen_g: set[str] = set()
        diff_s: list[str] = []
        diff_g: list[str] = []

        if len(s) != len(goal):
            return False
        for idx, val_g in enumerate(goal):
            val_s = s[idx]
            if val_s in seen_s or val_g in seen_g:
                repeated = True
            seen_s.add(val_s)
            seen_g.add(val_g)
            if val_g != val_s:
                diff_s.append(val_s)
                diff_g.append(val_g)

        if len(diff_s) == 0 and repeated:
            return True
        if len(diff_s) == 2 and diff_s[0] == diff_g[1] and diff_s[1] == diff_g[0]:
            return True

        return False


if __name__ == "__main__":
    sol = Solution()
    assert sol.buddyStrings("ab", "ba")
    assert sol.buddyStrings("aa", "aa")
