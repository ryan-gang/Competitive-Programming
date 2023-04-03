class Solution:
    # Runtime: 448 ms, faster than 92.75%.
    # Memory Usage: 20.9 MB, less than 60.46%.
    # T : O(NLogN), S : O(N) ; In py, the sort method uses the Timsort
    # algorithm, which is a combination of Merge Sort and Insertion Sort and
    # uses O(n) additional space.
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        """
        Greedy.
        Try to pair the heaviest guy with the lightest guy, if this pairing
        doesn't work the heaviest guy has to go alone.
        """
        people.sort()

        lo, hi, boats = 0, len(people) - 1, 0
        while lo <= hi:
            if people[hi] + people[lo] <= limit:
                lo += 1
            boats += 1
            hi -= 1
        boats += lo == hi

        return boats


if __name__ == "__main__":
    sol = Solution()
    assert sol.numRescueBoats(people=[3, 2, 2, 1], limit=3) == 3
    assert sol.numRescueBoats(people=[3, 5, 3, 4], limit=5) == 4
