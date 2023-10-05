from collections import defaultdict
import string


class Solution:
    # T : O(NM + M*MLogM), S : O(M^2)
    # N : len(votes), M : len(votes[0]) <= 26
    # Atmost there can be 26 keys in the dict, with an array of length 26 as the value.
    def rankTeams(self, votes: list[str]) -> str:
        """
        A single vote is constrained to 26 chars. So, a single character can
        occur in 26 different positions. Across all the votes, we just need to
        count the positions where each of the characters are occuring. And then
        sort it based on the positions.
        """
        d: dict[str, list[int]] = defaultdict(lambda: [0] * 27)
        # First 26 are positions in a single vote.
        # The last index is to break a tie.
        # We put the char's -ordinal there.
        # Because in case of a tie we want it sorted in asc.
        # d["A"] = [count of how many times "A" appeared in a particular position
        # across all votes]

        k = len(votes[0])
        for char in string.ascii_uppercase:
            d[char][-1] = -(ord(char) - 65)
        for vote in votes:
            for idx, char in enumerate(vote):
                d[char][idx] += 1

        keys = sorted(d, key=d.get, reverse=True)
        return "".join(keys)[:k]
