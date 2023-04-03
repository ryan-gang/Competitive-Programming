from bisect import bisect_left


class Solution:
    # Runtime:  ms, faster than %.
    # Memory Usage:  MB, less than %.
    # T : O(MLogM + NLogM), S : O(M) ; Sorting potions, and for N items in
    # spells, binary search each takes O(LogM).
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        """
        Sort potions, and then binary search for the appropriate potions, for
        each spell.
        """
        out: list[int] = []
        potions.sort()
        n = len(potions)
        for spell in spells:
            required = success / spell
            idx = bisect_left(potions, required)
            if idx == n:
                prods = 0
            else:
                prods = n - idx
            out.append(prods)

        return out

    # Runtime: 1356 ms, faster than 71.27%.
    # Memory Usage: 42.9 MB, less than 9.30%.
    #  T : O(NLogN+MLogM+N+M), S : O(N) ; Sorting both, and then single
    #  iteration of both arrays. Extra space for sorting.
    def successfulPairs1(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        """
        Sort both spells and potions, and then using 2 pointers match spells
        with their potions. As the spells only keep on growing larger, our
        required potion keeps on getting smaller."""
        spells_idx: list[tuple[int, int]] = [(val, idx) for idx, val in enumerate(spells)]
        potions.sort()
        spells_idx.sort()
        out: list[int] = [0 for _ in range(len(spells_idx))]
        idx = len(potions) - 1
        m = len(potions) - 1
        for spell, i in spells_idx:
            while idx >= 0 and spell * potions[idx] >= success:
                idx -= 1

            out[i] = m - idx

        return out
