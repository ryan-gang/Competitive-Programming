from heapq import heappushpop, heappush


class Solution:
    """
    To divide the marbles into `k` buckets, we need to put `k-1` dividers inside
    the weights array. As the cost depends on only the starting and ending
    marble, we can ignore the rest of the subarray, and just keep a track of the
    `score` for each divider that we put in the `weights` array. And then we can
    greedily choose the most and least optimal dividers and return their
    difference.
    We can store the score for all the dividers in an array, O(N) space, then
    sort it and take the first K-1 and last K-1 dividers.
    Or more optimally keep a K length heap, for the max values, and the min
    values. O(K) space requirement.
    Note : We willingly ignore the first and last weight, which will inevitably
    be there in the score for both the distributions, and hence cancel out.
    """

    # Runtime: 836 ms, faster than 31.19%.
    # Memory Usage: 30.2 MB, less than 16.97%.
    # T : O(N), S : O(K) ; We only keep 2 K-length heaps.
    def putMarbles(self, weights: list[int], k: int) -> int:
        min_heap = []
        max_heap = []

        max_size = k - 1

        for i in range(len(weights) - 1):
            add = weights[i] + weights[i + 1]
            if len(min_heap) >= max_size:
                heappushpop(min_heap, add)
                heappushpop(max_heap, -add)
            else:
                heappush(min_heap, add)
                heappush(max_heap, -add)

        return sum(min_heap) + sum(max_heap)

    # Runtime: 751 ms, faster than 61.93%.
    # Memory Usage: 29.3 MB, less than 24.31%.
    # T : O(N), S : O(N) ; N length array is stored.
    def putMarbles1(self, weights: list[int], k: int) -> int:
        values: list[int] = []

        for i in range(len(weights) - 1):
            add = weights[i] + weights[i + 1]
            values.append(add)

        values.sort()
        K = k - 1
        return sum(values[-K:]) - sum(values[:K]) if K else 0


if __name__ == "__main__":
    sol = Solution()
    assert sol.putMarbles(weights=[1, 3, 5, 1], k=2) == 4
    assert sol.putMarbles(weights=[1, 3], k=2) == 0
    assert sol.putMarbles(weights=[25, 74, 16, 51, 12, 48, 15, 5], k=1) == 0
