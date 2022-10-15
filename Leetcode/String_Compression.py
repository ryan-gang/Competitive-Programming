from typing import List, Tuple


# Runtime: 78 ms, faster than 77.67% of Python3 online submissions.
# Memory Usage: 14.2 MB, less than 31.27% of Python3 online submissions.
class Solution:
    @staticmethod
    def _break_streak(
        chars: List[str], write_idx: int, prev: str, out: str, streak: int
    ) -> Tuple[int, int, str]:
        """Everytime we need to break a streak, we call this method.
        But also at the end of the string, this code block has to be called. So created a method."""
        chars[write_idx] = prev
        write_idx += 1
        out += str(prev)
        if streak > 1:
            out += str(streak)
            if streak > 9:
                for _ in str(streak):
                    chars[write_idx] = _
                    write_idx += 1
            else:
                chars[write_idx] = str(streak)
                write_idx += 1
        streak = 1

        return streak, write_idx, out

    def compress(self, chars: List[str]) -> int:
        prev = None
        streak = 0
        out = ""
        n = len(chars)
        write_idx = 0

        for idx in range(1, n + 1):
            curr = chars[idx - 1]
            if (prev != curr) and prev:
                streak, write_idx, out = Solution._break_streak(chars, write_idx, prev, out, streak)
            else:
                streak += 1
            prev = curr

        _, write_idx, out = Solution._break_streak(chars, write_idx, prev, out, streak)

        print(out, chars, write_idx)
        return write_idx


if __name__ == "__main__":
    sol = Solution()
    assert sol.compress(chars=["a", "a", "b", "b", "c", "c", "c"]) == 6
    assert (
        sol.compress(chars=["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]) == 4
    )
