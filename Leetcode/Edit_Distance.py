class Solution:
    """
    Let D(i,j) be the edit distance for strings X[:i] and Y[:j]
    So, our output, edit distance for strings X and Y will be D(m,n)

    D(i, 0) = i (For all substrings of X, and an empty string, the edit distance
    is the length of the substring.)
    D(0, j) = j
    (for i in range(m) and j in range(n))
    For any index, we can make 3 possible changes.
    - Insertion. We add a new char at the jth index. So our value is D[i-1, j]
    - Deletion. We discard the char at jth index. So our value is D[i, j-1]
    - Substitution. We see if X[i] and Y[j] are identical, in that case substitution cost is 0.
    Else it is 1. In this case. Our score is D[i-1, j-1] + substitution_cost.
    We can implement the bottom up approach, and it should be fine.
    Ref : https://web.stanford.edu/class/cs124/lec/med.pdf
    """

    # Runtime: 194 ms, faster than 30.90%.
    # Memory Usage: 17.6 MB, less than 29.79%.
    # T : O(M*N), S : O(M*N)
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        table = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            table[i][0] = i
        for j in range(n + 1):
            table[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                table[i][j] = min(
                    table[i - 1][j] + 1,
                    table[i][j - 1] + 1,
                    table[i - 1][j - 1] + int(word1[i - 1] != word2[j - 1]),
                )
        return table[-1][-1]


if __name__ == "__main__":
    sol = Solution()
    assert sol.minDistance(word1="horse", word2="ros") == 3
    assert sol.minDistance(word1="intention", word2="execution") == 5
