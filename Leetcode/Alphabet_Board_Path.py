from typing import Dict, List, Tuple


class Solution:
    """
    Clean optimal solution, great from a prod perspective.
    """

    def __init__(self) -> None:
        o = 97
        self.letter_to_coords: Dict[str, Tuple[int, int]] = {}
        self.r_mapping = {-1: "D", 1: "U"}
        self.c_mapping = {-1: "R", 1: "L"}

        for r in range(6):
            for c in range(5):
                if o <= 122:
                    self.letter_to_coords[chr(o)] = (r, c)
                    o += 1

    def travel(self, r1: int, c1: int, r2: int, c2: int) -> str:
        out = ""
        dr, dc = r1 - r2, c1 - c2
        if r1 == 5:
            out += self.move_1d(dr, self.r_mapping)
            out += self.move_1d(dc, self.c_mapping)
        else:
            out += self.move_1d(dc, self.c_mapping)
            out += self.move_1d(dr, self.r_mapping)
        return out

    def move_1d(self, delta: int, move_letter_mapping: Dict[int, str]):
        out: List[str] = []
        while delta != 0:
            move = int(delta / abs(delta))
            delta -= move
            out.append(move_letter_mapping[move])
        return "".join(out)

    def alphabetBoardPath(self, target: str) -> str:
        out: List[str] = []
        curr = 0, 0
        for char in target:
            coords: Tuple[int, int] = self.letter_to_coords[char]
            out.append(self.travel(*curr, *coords))
            curr = coords

        print("!".join(out) + "!")
        return "!".join(out) + "!"

    def alphabetBoardPath1(self, target: str):
        m = {c: [i / 5, i % 5] for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")}
        x0, y0 = 0, 0
        res: List[str] = []
        for c in target:
            x, y = m[c]
            if y < y0:
                res.append("L" * int(y0 - y))
            if x < x0:
                res.append("U" * int(x0 - x))
            if x > x0:
                res.append("D" * int(x - x0))
            if y > y0:
                res.append("R" * int(y - y0))
            res.append("!")
            x0, y0 = x, y
        return "".join(res)


if __name__ == "__main__":
    sol = Solution()
    assert sol.alphabetBoardPath(target="leet") == "RDD!RRRUU!!DDD!"
    assert sol.alphabetBoardPath(target="code") == "RR!RRDD!LUU!R!"
    assert sol.alphabetBoardPath(target="zdz") == "DDDDD!UUUUURRR!LLLDDDDD!"
