from heapq import heappush, heappop
from math import isclose


class Solution:
    """
    For each worker we calculate their wage / quality ratio. For a given ratio
    R, all workers with ratio less than R will be paid according to their
    quality, so wage will be scaled up and everybody will get paid over their
    expected wage.

    So our task essentially is to figure out the optimal ratio R, and find out
    the k workers with the lowest quality.

    In our code, we loop over all the ratios in ascending order, and keep the K
    lowest quality values in a heap, changing them as required. And then
    multiple R with the sum of K qualities to get the total cost.
    """
    # T : O(NLogN), S : O(N)
    def mincostToHireWorkers(self, quality: list[int], wage: list[int], k: int) -> float:
        DIGITS = 16
        wbq = [round(w / q, DIGITS) for (w, q) in zip(wage, quality)]  # wage per unit quality

        A = sorted([(i, j) for i, j in zip(wbq, quality)])

        heap: list[tuple[int, float]] = []
        curr_q: int = 0
        min_cost = float("inf")
        for ratio, q in A:
            heappush(heap, (-q, ratio))
            curr_q += q
            if len(heap) == k:
                min_cost = min(min_cost, curr_q * ratio)
                pop_q, _ = heappop(heap)
                curr_q -= -pop_q

        return min_cost


if __name__ == "__main__":
    sol = Solution()
    assert sol.mincostToHireWorkers(quality=[10, 20, 5], wage=[70, 50, 30], k=2) == 105.00
    assert isclose(
        sol.mincostToHireWorkers(quality=[3, 1, 10, 10, 1], wage=[4, 8, 2, 2, 7], k=3),
        30.66667,
        abs_tol=10**-5,
    )
