class Solution:
    # T : O(N), S : O(1)
    def judgeCircle(self, moves: str) -> bool:
        mapping: dict[str, tuple[int, int]] = {
            "R": (1, 0),
            "L": (-1, 0),
            "U": (0, 1),
            "D": (0, -1),
        }  # X-Y coordinates
        x, y = 0, 0
        for move in moves:
            dx, dy = mapping[move]
            x, y = x + dx, y + dy

        return not x and not y

    def judgeCircleEditorial(self, moves: str):
        x = y = 0
        for move in moves:
            if move == "U":
                y -= 1
            elif move == "D":
                y += 1
            elif move == "L":
                x -= 1
            elif move == "R":
                x += 1

        return x == y == 0
