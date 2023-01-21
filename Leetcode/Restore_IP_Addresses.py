import itertools
from typing import List


class Solution:
    # Runtime: 64 ms, faster than 34.17%.
    # Memory Usage: 13.9 MB, less than 31.50%.
    # T : O(3 ** N), S : O(N)
    def restoreIpAddresses(self, S: str) -> List[str]:
        """Use backtracking for such a small search space is not required."""
        n = len(S)
        all_ips: List[str] = []
        if not 4 <= n <= 12:
            return all_ips

        def dfs(ip: List[str], idx: int):
            """idx will be processed now."""
            if len(ip) > 4:
                return
            if len(ip) == 4 and idx == n:
                all_ips.append(".".join(ip))
                return
            for i in range(idx + 1, min(idx + 4, n + 1)):
                val = S[idx:i]
                if not val.startswith("0") or val == "0":
                    if 0 <= int(val) <= 255:
                        ip.append(val)
                        dfs(ip, i)
                        ip.pop()

        dfs([], 0)
        return all_ips

    """Bruteforce works equally well. Because we can have at most 12C3 combinations.
    Very elegant solution, I have to say. NOTE."""

    @staticmethod
    def leading_0(string: str):
        return string[0] == "0" and string != "0"

    @staticmethod
    def valid(part: str):
        return not Solution.leading_0(part) and int(part) <= 255

    @staticmethod
    def valid_ip(nums: List[str]):
        return all(Solution.valid(part) for part in nums)

    def restoreIpAddresses1(self, s: str) -> List[str]:
        ret: List[str] = []
        for i, j, k in itertools.combinations(range(1, len(s)), 3):
            # range(1, len(s)) is essentially used as a proxy for list s, these are the indices of s.
            # Out of all possible indices we choose 3 at a time.
            # first one is upto i, so it can't be zero.
            ip = [s[:i], s[i:j], s[j:k], s[k:]]
            if Solution.valid_ip(ip):
                ret.append(".".join(ip))
        return ret
