class Solution:
    # T : O(N), S : O(1)
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        # Calculate slope at each point, and make sure it is same at every location.
        slope = None
        for i in range(1, len(coordinates)):
            x1, y1 = coordinates[i - 1]
            x2, y2 = coordinates[i]

            if x2 - x1 != 0:
                sl = (y2 - y1) / (x2 - x1)
            else:
                sl = float("inf")
            sl = round(sl, 2)
            if slope is None:
                slope = sl
            elif slope != sl:
                return False

        return True
