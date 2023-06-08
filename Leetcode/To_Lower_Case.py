class Solution:
    # T : O(N), S : O(N)
    def toLowerCase(self, s: str) -> str:
        # For chars with ascii values between 'A' to 'Z', map them to 'a' to 'z'.
        out: list[str] = []
        for char in s:
            if ord("A") <= ord(char) <= ord("Z"):
                out.append(chr(ord(char) + ord("a") - ord("A")))
            else:
                out.append(char)
        return "".join(out)


if __name__ == "__main__":
    sol = Solution()
    assert sol.toLowerCase(s="Hello") == "hello"
