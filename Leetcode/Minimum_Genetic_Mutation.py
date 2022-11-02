from collections import deque
from typing import List


class Solution:
    """
    For each gene in the bank compare with current gene, if hamming distance == 1, then
    make this the next mutated version of current gene. Until we reach end we keep on repeating.
    Our actual algo is a BFS, which is preferred while searching for shortest distances, because
    all nodes that are X distance away will be checked before going for the X+1 distance away node.
    Also, this algo works here because bank is guaranteed to have less than 10 genes,
    but that wont be the case in real life, where it should be preferable to generate all
    possible mutations from current gene and check if it is in bank.
    """

    @staticmethod
    def hamming_distance(start: str, end: str):
        n = len(start)
        count = 0
        for idx in range(n):
            if start[idx] != end[idx]:
                count += 1
        return count

    # Ref : 2768793/Python3-Python-BFS-Better-memory-complexity-by-Defining-adjacency-from-the-bank
    # Runtime: 62 ms, faster than 28.70% of Python3 online submissions.
    # Memory Usage: 13.9 MB, less than 86.98% of Python3 online submissions.
    # For each element in Bank, we check with all other elements in Bank,
    # and everytime we find the hamming distance.
    #  T : O(B x B x N), S : O(B)
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        queue = deque([start])
        visited = set(start)
        mutations = 0

        while queue:
            for _ in range(len(queue)):
                gene = queue.popleft()
                if gene == end:
                    return mutations
                for variant in bank:
                    if Solution.hamming_distance(gene, variant) == 1:
                        if variant not in visited:
                            queue.append(variant)
                            visited.add(variant)

            mutations += 1
        return -1

    """
    We generate all the possible genes (at a hamming distance of 1 from current node),
    from current gene and check if it is in Bank, if yes then we recurse on this.
    The entire thing is done as a BFS.
    """
    # Runtime: 62 ms, faster than 28.70% of Python3 online submissions.
    # Memory Usage: 14 MB, less than 37.43% of Python3 online submissions.
    # m = bases, n = chars in genes
    # m^n possible states, for each state we do m * n work, O(n) work for lists
    # T : O(m^n x m x n^2), S : O(m^n)
    def minMutation2(self, start: str, end: str, bank: List[str]) -> int:
        BASES = ["A", "T", "G", "C"]
        queue = deque([start])
        visited = set(start)
        mutations = 0

        while queue:
            print(queue)
            for _ in range(len(queue)):
                print(_)
                gene = queue.popleft()
                if gene == end:
                    print(mutations)
                    return mutations
                for idx, base in enumerate(gene):
                    gene_edit = list(gene)
                    for BASE in BASES:
                        if base != BASE:
                            gene_edit[idx] = BASE
                            gene_edited = "".join(gene_edit)
                            if gene_edited in bank and gene_edited not in visited:
                                queue.append(gene_edited)
                                visited.add(gene_edited)

            mutations += 1
        return -1


if __name__ == "__main__":
    sol = Solution()
    assert (
        sol.minMutation(start="AACCGGTT", end="AAACGGTA", bank=["AACCGGTA", "AACCGCTA", "AAACGGTA"])
        == 2
    )

    assert (
        sol.minMutation(start="AAAAACCC", end="AACCCCCC", bank=["AAAACCCC", "AAACCCCC", "AACCCCCC"])
        == 3
    )

    assert (
        sol.minMutation(
            "AAAACCCC",
            "CCCCCCCC",
            [
                "AAAACCCA",
                "AAACCCCA",
                "AACCCCCA",
                "AACCCCCC",
                "ACCCCCCC",
                "CCCCCCCC",
                "AAACCCCC",
                "AACCCCCC",
            ],
        )
        == 4
    )

    assert sol.minMutation(
        "AAAAAAAA",
        "CCCCCCCC",
        [
            "AAAAAAAA",
            "AAAAAAAC",
            "AAAAAACC",
            "AAAAACCC",
            "AAAACCCC",
            "AACACCCC",
            "ACCACCCC",
            "ACCCCCCC",
            "CCCCCCCA",
        ],
    )
