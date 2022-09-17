import heapq
from typing import List


# Runtime: 971 ms, faster than 33.88%.
# Memory Usage: 28.6 MB, less than 54.37%.
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        heapq.heapify(heap)

        for i in range(len(heights) - 1):
            curr, next = heights[i], heights[i + 1]
            diff = next - curr
            if diff < 0:
                continue
            else:
                bricks -= diff
                negate_diff = diff * -1
                heapq.heappush(heap, negate_diff)

            if bricks < 0:
                # Get the highest jump till now use a ladder for that jump.
                highest = -1 * heapq.heappop(heap)
                bricks += highest
                if ladders > 0:
                    ladders -= 1
                else:
                    return i
        return len(heights) - 1


sol = Solution()
print(sol.furthestBuilding(heights=[4, 12, 2, 7, 3, 18, 20, 3, 19], bricks=10, ladders=2))
