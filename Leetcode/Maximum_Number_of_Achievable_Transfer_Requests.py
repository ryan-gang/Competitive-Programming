class Solution:
    # T : O(2^N * M), S : O(N + M)
    # N = len(requests), M = n
    # We try all 2 ^ N possibilities from requests
    # array and check to see if the scenario is possible.
    def maximumRequests(self, n: int, requests: list[list[int]]) -> int:
        answer = 0

        def recurse(index: int, taken: int, changes: list[int]):
            nonlocal answer
            if index == len(requests):
                if all([i == 0 for i in changes]):
                    answer = max(answer, taken)
                return
            _from, _to = requests[index]
            # Take the request at index.
            changes[_from] -= 1
            changes[_to] += 1
            recurse(index + 1, taken + 1, changes)

            changes[_from] += 1
            changes[_to] -= 1
            # This resetting changes can be skipped, and `not_take` part done
            # first, but then at every step changes[::] has to be sent. Taking
            # more time and space.
            # Don't take the request at index.
            recurse(index + 1, taken, changes)

        recurse(0, 0, [0] * n)
        return answer

    # T : O(2^N * M), S : O(N + M)
    # All the 2 ^ N scenarios can be modelled using all the integers from 0 to 2
    # ^ N in binary. For each scenario we create the movements array and then
    # check if its feasible.
    def maximumRequests1(self, n: int, requests: list[list[int]]) -> int:
        answer = 0
        for mask in range(1 << len(requests)):
            count = 0  # Requests processed
            changes = [0] * n
            idx = 0
            while mask:
                if mask & 1:
                    _from, _to = requests[idx]
                    changes[_from] -= 1
                    changes[_to] += 1
                    count += 1
                idx += 1
                mask >>= 1
            if all([i == 0 for i in changes]):
                answer = max(answer, count)

        return answer


if __name__ == "__main__":
    sol = Solution()
    assert sol.maximumRequests1(5, [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]) == 5
