class Solution:
    # T : O(LogN), S : O(1)
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        def condition(x: int) -> bool:
            return letters[x] > target

        lo, hi = 0, len(letters)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if condition(mid):
                hi = mid
            else:
                lo = mid + 1

        return letters[lo] if 0 <= lo < len(letters) else letters[0]


if __name__ == "__main__":
    sol = Solution()
    assert sol.nextGreatestLetter(letters=["c", "f", "j"], target="a") == "c"
    assert sol.nextGreatestLetter(letters=["c", "f", "j"], target="c") == "f"
    assert sol.nextGreatestLetter(letters=["x", "x", "y", "y"], target="z") == "x"
