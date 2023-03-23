class Solution:
    # Runtime: 24 ms, faster than 94.41%.
    # Memory Usage: 13.8 MB, less than 45.27%.
    # T : O(1), S : O(1)
    def passThePillow(self, n: int, time: int) -> int:
        move, start = 1, 1  # Initially we move towards right, from 1.
        b = n - 1  # blocks of space to traverse.
        dir_changes = time // (b)  # How many times we change direction.
        position = time % b  # From the end how many places to move.
        if dir_changes % 2:  # If odd number of changes, we need to come back to front.
            move *= -1  # Move backwards.
            start = n  # Start from the end.
        start += move * position
        return start


if __name__ == "__main__":
    sol = Solution()
    assert sol.passThePillow(n=4, time=5) == 2
    assert sol.passThePillow(n=3, time=2) == 3
