from collections import defaultdict
from bisect import bisect_right


# get() self implementation of bin search.
# Runtime: 2130 ms, faster than 10.35% of Python3 online submissions.
# Memory Usage: 72.2 MB, less than 38.03% of Python3 online submissions.

# get2() LC implementation of bin search.
# Runtime: 2053 ms, faster than 13.84% of Python3 online submissions.
# Memory Usage: 71.7 MB, less than 53.69% of Python3 online submissions.

# get3() Python bin search function.
# Runtime: 1563 ms, faster than 38.03% of Python3 online submissions.
# Memory Usage: 70.8 MB, less than 86.55% of Python3 online submissions.
class TimeMap:
    """
    Use a hashmap, for every key, keep a list of values, with their corresponding timestamps.
    Dictionary(key, List(Tuple(timestamp, value)))
    For every "get", we can first check if we have any values for this key, else return "".
    If we have values, we can perform a binary search on the values,
    based on timestamp. (As it is given that the timestamps will be in sorted order.)
    We iteratively check if we have got an index, where values[index] <= timestamp
    but the next element is > timestamp. This binary search implementation is a bit clunky.
    We could have simplified this, or just used the library function.
    """

    def __init__(self):
        self.map = defaultdict(list)

    # T : O(L) for hashing string key. O(1) amortized for insertion.
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    # T : O(L) for hashing. O(log M) for binary search, where M is the length of vals array.
    # Self implementation, rudimentary binary search.
    def get(self, key: str, timestamp: int) -> str:
        values = self.map[key]
        n = len(values) - 1
        lo, hi = 0, n
        value = ""
        while lo <= hi:
            mid = (lo + hi) // 2
            middle = values[mid][0]
            if mid < n:
                middle_right = values[mid + 1][0]
            if middle == timestamp:
                value = values[mid][1]
                break
            elif middle <= timestamp and (mid == n or middle_right > timestamp):
                value = values[mid][1]
                break
            elif middle < timestamp:
                lo = mid + 1
            else:
                hi = mid - 1

        return value

    # Leetcode editorial.
    def get2(self, key: str, timestamp: int) -> str:
        # If the 'key' does not exist in dictionary we will return empty string.
        if key not in self.map:
            return ""

        # If timestamp, less than the lowest timestamp in our values array, for this key.
        if timestamp < self.map[key][0][0]:
            return ""

        left = 0
        right = len(self.map[key])

        while left < right:
            mid = (left + right) // 2
            if self.map[key][mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid

        # If iterator points to first element it means, no time <= timestamp exists.
        return "" if right == 0 else self.map[key][right - 1][1]

    def get3(self, key: str, timestamp: int) -> str:
        # If the 'key' does not exist in dictionary we will return empty string.
        if key not in self.map:
            return ""

        middle = bisect_right(self.map[key], timestamp, key=lambda item: item[0])
        if middle == 0:
            return ""
        # If iterator points to first element it means, no time <= timestamp exists.
        return self.map[key][middle - 1][1]


if __name__ == "__main__":
    map = TimeMap()
    map.set("foo", "bar", 10)
    map.set("foo", "bar2", 20)
    print(map.map)
    print(map.get3("foo", 5))
    print(map.get3("foo", 10))
    print(map.get3("foo", 15))
    print(map.get3("foo", 20))
    print(map.get3("foo", 25))
