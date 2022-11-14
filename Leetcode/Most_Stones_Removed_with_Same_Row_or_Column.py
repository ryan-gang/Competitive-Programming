from typing import List
from StarterCode.Union_Find import Union

"""
Ref : discuss/197668/Count-the-Number-of-Islands-O(N)
I have used a dictionary to keep track of the mapping between coordinates and array indices.
People are doing i and ~j, -(j+1). As their indices.
"""


class Solution:
    """
    Here, we put each stone into an index of the array, which is the parents array of a DSU.
    Then for every stone we union it with the "row parent" and "col parent",
    for each row we assign a row parent, with which we union all the stones in that row.
    Basically it's a proxy for the row index and col index.
    And we return the number of successful unions, for every union we can remove a stone.
    """

    # Runtime: 229 ms, faster than 84.09% of Python3 online submissions.
    # Memory Usage: 14.7 MB, less than 56.91% of Python3 online submissions.
    def removeStones(self, stones: List[List[int]]) -> int:
        n, idx = len(stones), 0
        uf = Union(n)
        mapping_stone_idx = {}

        rows, cols = {}, {}

        for stone in stones:
            r, c = stone
            if not rows.get(r, 0):
                rows[r] = stone
            if not cols.get(c, 0):
                cols[c] = stone

            mapping_stone_idx[(r, c)] = idx
            uf.new(idx)
            idx += 1

        count = 0
        for stone in stones:
            i, j = stone
            c = tuple(cols[j])
            r = tuple(rows[i])
            curr_node = mapping_stone_idx[(i, j)]
            row_parent = mapping_stone_idx[r]
            col_parent = mapping_stone_idx[c]

            if uf.union(curr_node, row_parent):
                count += 1
            if uf.union(curr_node, col_parent):
                count += 1
        return count


if __name__ == "__main__":
    sol = Solution()
    assert sol.removeStones(stones=[[0, 1], [1, 2], [1, 3], [3, 3], [2, 3], [0, 2]]) == 5
    assert sol.removeStones(stones=[[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]) == 5
    assert sol.removeStones(stones=[[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]) == 3
    assert sol.removeStones(stones=[[0, 0]]) == 0
