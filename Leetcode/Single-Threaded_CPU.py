from heapq import heappush, heappop
from typing import List


class Solution:
    # Unoptimal. 37/39 TC Passed.
    # Only problem, is that time is being incremented by 1 each iteration.
    # This leads to TLE, for huuuge time intervals.
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # tasks -> enqueue, processing

        tasks = [tasks[idx] + [idx] for idx in range(len(tasks))]  # enqueue, processing, idx
        tasks.sort()
        ready, order = [], []
        idx = completed = 0
        time = min(tasks)[0] - 1
        while completed < len(tasks):
            while idx < len(tasks) and tasks[idx][0] <= time:
                task = tasks[idx]
                heappush(ready, [task[1], task[2]])  # processing, idx
                idx += 1
            if ready:
                processing_task = heappop(ready)
                time += processing_task[0] - 1
                # print(processing_task[1])
                order.append(processing_task[1])
                completed += 1
            time += 1

        return order

    # Runtime: 1997 ms, faster than 91.30%.
    # Memory Usage: 63.4 MB, less than 18.23%.
    # T : O(NLogN), S : O(N)
    # Sorting, and heapppush, heappop for all N elements.
    # Ref : /1163980/python-sort-then-heap/?orderBy=most_votes
    # https://archive.md/BI2Ap
    def getOrder2(self, tasks: List[List[int]]) -> List[int]:
        order = []
        tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])
        idx = 0
        ready = []
        time = tasks[0][0]
        while len(order) < len(tasks):
            while (idx < len(tasks)) and (tasks[idx][0] <= time):
                heappush(ready, (tasks[idx][1], tasks[idx][2]))  # (processing_time, original_index)
                idx += 1
            if ready:
                t_diff, original_index = heappop(ready)
                time += t_diff
                order.append(original_index)
            elif idx < len(tasks):
                time = tasks[idx][0]
        return order


if __name__ == "__main__":
    sol = Solution()
    assert sol.getOrder(tasks=[[1, 2], [2, 4], [3, 2], [4, 1]]) == [0, 2, 3, 1]
    assert sol.getOrder(tasks=[[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]) == [4, 3, 2, 0, 1]
    assert sol.getOrder(tasks=[[1, 2], [2, 4], [3, 2], [4, 1], [1, 4], [1, 5]]) == [
        0,
        2,
        3,
        1,
        4,
        5,
    ]
    assert sol.getOrder(tasks=[[1000000000, 1000000000]]) == [0]
    assert sol.getOrder(tasks=[[1, 2], [2, 4], [3, 2], [4, 1], [10000000, 10000000]]) == [
        0,
        2,
        3,
        1,
        4,
    ]
    assert sol.getOrder(
        tasks=[
            [1, 2],
            [2, 4],
            [3, 2],
            [4, 1],
            [10000000, 10000002],
            [10000000, 10000001],
            [10000000, 10000000],
        ]
    ) == [0, 2, 3, 1, 6, 5, 4]
    assert sol.getOrder([[100, 100], [1000000000, 1000000000]]) == [0, 1]
