# TODO Booth's Algorithm
# TODO https://cp-algorithms.com/string/lyndon_factorization.html


"""
Algorithm
If k = 1, only rotations of s are possible, and the answer is the lexicographically
smallest rotation.
If k > 1, any permutation of s is possible, and the answer is the letters of s
written in lexicographic order.

T : O(N^2) where N is the length of s.
If k = 1, we need O(N) time to build each new string and O(N) time to check whether it's the
lexicographically smallest string among the strings generated so far. In total, there are N such
different strings to build and check. Therefore, the time complexity for this case is O(N^2).
If k > 1, we need to convert our given string to an array of characters (this costs O(N) time),
then sort the newly obtained array (sorting takes O(Nlog⁡N) time), and build the output string
from the sorted array which takes O(N) time.
Thus, the worst-case scenario is when k is 1, so the overall time complexity of the
solution is O(N^2).

S : O(N).
If k = 1, we need the space to store only two strings: the lexicographically smallest string
found so far and a newly built string, that will be compared to the lexicographically smallest
string. This requires O(N) space.
If k > 1, we need O(N) space to store the character array. Other than that, sorting the array
requires O(log⁡N) additional space for Java and O(N) additional space for Python.
Therefore, the overall space complexity of the solution is O(N).
"""


# Runtime: 69 ms, faster than 22.62% of Python3 online submissions.
# Memory Usage: 13.9 MB, less than 39.29% of Python3 online submissions.
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            return min(s[i:] + s[:i] for i in range(len(s)))
        else:
            return "".join(sorted(s))
