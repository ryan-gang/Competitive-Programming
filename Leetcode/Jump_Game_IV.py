from collections import defaultdict, deque


class Solution:
    # Can also use bidirectional bfs.
    def minJumps(self, arr: list[int]) -> int:
        queue = deque([0])
        jumps = 0
        N = len(arr) - 1
        d: dict[int, list[int]] = defaultdict(list)
        for idx, val in enumerate(arr):
            d[val].append(idx)

        visited: set[int] = set()
        # Naive BFS, with a simple change.
        # At every iteration, we can jump to the same valued indices also, so to accomodate
        # that, and not jump backwards and forwards recursively, we make a jump to same valued
        # index, only ONCE, the first time (when the number of jumps is least, most optimal
        # value), and then delete that key from the dict, where we store the indices for same
        # valued key.
        while queue:
            for _ in range(len(queue)):
                idx = queue.popleft()
                val = arr[idx]
                if idx == N:
                    return jumps
                if idx - 1 > 0 and idx - 1 not in visited:
                    queue.append(idx - 1)
                    visited.add(idx - 1)
                if idx + 1 <= N and idx + 1 not in visited:
                    queue.append(idx + 1)
                    visited.add(idx + 1)
                for i in d[val]:
                    if i != idx:
                        queue.append(i)
                del d[val]

            jumps += 1

        return jumps


if __name__ == "__main__":
    sol = Solution()
    assert (sol.minJumps(arr=[100, -23, -23, 404, 100, 23, 23, 23, 3, 404])) == 3
    assert (sol.minJumps(arr=[7])) == 0
    assert (sol.minJumps(arr=[7, 6, 9, 6, 9, 6, 9, 7])) == 1
    assert (sol.minJumps(arr=[7, 7, 2, 1, 7, 7, 7, 3, 4, 1])) == 3
