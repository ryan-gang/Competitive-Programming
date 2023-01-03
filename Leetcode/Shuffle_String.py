from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        out = [""] * len(s)
        for idx, val in zip(indices, s):
            out[idx] = val

        return "".join(out)
