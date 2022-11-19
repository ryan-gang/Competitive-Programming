from collections import deque


class Solution:
    """
    COULDN'T CHECK CODE AS LOCKED IN LC.
    BFS over the chessboard, to check if we reach the target.
    To optimise the code, we also check that we always stay in the same quadrant as the target.
    And we keep a track of visited cells, so as to not get stuck in a loop.
    """

    def __init__(self) -> None:
        self.MOVES = [
            (1, 2),
            (2, 1),
            (1, -2),
            (2, -1),
            (-1, -2),
            (-2, -1),
            (-1, 2),
            (-2, 1),
        ]

    @staticmethod
    def get_quadrant(x, y):
        if x > 0 and y > 0:
            return "1"
        elif x > 0 and y < 0:
            return "2"
        elif x < 0 and y < 0:
            return "3"
        else:
            return "4"

    def minKnightMoves(self, X, Y):
        queue = deque()
        queue.append((0, 0))
        count = 0
        visited = set()

        while 1:
            print(count, queue)
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for move in self.MOVES:
                    r, c = x + move[0], y + move[1]
                    if (r, c) == (X, Y):
                        return count + 1
                    if (r, c) not in visited:
                        if Solution.get_quadrant(X, Y) == Solution.get_quadrant(r, c):
                            queue.append((r, c))
                            visited.add((r, c))
            count += 1


sol = Solution()
assert (sol.minKnightMoves(X=5, Y=5)) == 4
assert (sol.minKnightMoves(X=2, Y=1)) == 1
assert (sol.minKnightMoves(X=29, Y=29)) == 20
