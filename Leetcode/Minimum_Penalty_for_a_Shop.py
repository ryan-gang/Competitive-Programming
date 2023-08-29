class Solution:
    # T : O(N), S : O(N)
    # Takes 3 passes over the entire length.
    def bestClosingTime(self, customers: str) -> int:
        open_penalty: list[int] = []
        closed_penalty: list[int] = [0]
        N = len(customers)

        # Generate a prefix sum array for N.
        # This array needs to be right shifted by one unit. (So the 0 in line 9)
        n_count = 0
        for idx, val in enumerate(customers):
            n_count += val == "N"
            closed_penalty.append(n_count)

        # Generate prefix sum array for Y.
        # This array needs to be left shifted by one unit. So the extra appending.
        y_count = N - n_count
        for idx, val in enumerate(customers):
            open_penalty.append(y_count)
            y_count -= val == "Y"
        open_penalty.append(0)

        min_penalty = N
        index = 0
        for idx in range(N + 1):
            penalty = open_penalty[idx] + closed_penalty[idx]
            if penalty < min_penalty:
                min_penalty = penalty
                index = idx

        return index

    """
    As we dont need the penalty value, just keeping track of the relative
    changes also work. And only takes 1 pass.
    """
    # T : O(N), S : O(1)
    def bestClosingTime2(self, customers: str) -> int:
        # Start with closing at hour 0 and assume the current penalty is 0.
        cur_penalty = min_penalty = 0
        earliest_hour = 0

        for i, ch in enumerate(customers):
            # If status in hour i is 'Y', moving it to open hours decrement
            # penalty by 1. Otherwise, moving 'N' to open hours increment
            # penalty by 1.
            if ch == "Y":
                cur_penalty -= 1
            else:
                cur_penalty += 1

            # Update earliest_hour if a smaller penalty is encountered
            if cur_penalty < min_penalty:
                earliest_hour = i + 1
                min_penalty = cur_penalty

        return earliest_hour


if __name__ == "__main__":
    sol = Solution()
    assert sol.bestClosingTime(customers="YYNY") == 2
