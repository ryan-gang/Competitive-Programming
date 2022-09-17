# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    flag = False
    if version > 17:
        flag = True
    return flag


class Solution:
    # Runtime: 41 ms, faster than 66.75% of Python3 online submissions.
    # Memory Usage: 13.8 MB, less than 61.83% of Python3 online submissions.
    # T : O(lgN), S : O(1)
    def firstBadVersion(self, n: int) -> int:
        lo, hi = 0, n
        while lo <= hi:
            mid = (lo + hi) // 2
            isBadCurrent = isBadVersion(mid)
            isBadPrevious = isBadVersion(mid - 1)
            if isBadCurrent and not isBadPrevious:
                return mid
            elif isBadCurrent:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1


sol = Solution()
sol.firstBadVersion(n=25)
