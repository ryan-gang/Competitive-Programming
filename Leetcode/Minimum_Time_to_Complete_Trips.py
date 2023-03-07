class Solution:
    # Runtime: 3125 ms, faster than 33%.
    # Memory Usage: 28.5 MB, less than 70.25%.
    # T : O(Nlog(M*K)), S : O(1), where N is the length of time,
    # M is the upper limit of totalTrips
    # and K is the maximum time taken by one trip.
    def minimumTime(self, time: list[int], totalTrips: int) -> int:
        """
        For a given elapsed time, we can figure out the total number
        of all concurrent trips possible with all our buses.
        So, we use this function as a key and binary search for our
        time elapsed, such that it is gte than the totalTrips.
        """
        lo, hi = 0, totalTrips * time[0]
        while lo < hi:
            elapsed = (hi + lo) // 2
            trips = sum(map(lambda time_needed: elapsed // time_needed, time))
            # Returns the number of trips possible, in the `elapsed` time period.
            # Based on this we can reduce or increase elapsed time.
            if trips >= totalTrips:
                hi = elapsed
            else:
                lo = elapsed + 1

        return lo


if __name__ == "__main__":
    sol = Solution()
    assert sol.minimumTime(time=[1, 2, 3], totalTrips=5) == 3
    assert sol.minimumTime(time=[2], totalTrips=1) == 2
    assert sol.minimumTime(time=[5, 10, 10], totalTrips=9) == 25
