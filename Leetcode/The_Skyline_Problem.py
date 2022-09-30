from collections import defaultdict

# Ref : https://github.com/mission-peace/interview/blob/master/python/geometry/skylinedrawing.py
# https://github.com/mission-peace/interview/blob/master/src/com/interview/geometry/SkylineDrawing.java
# https://www.youtube.com/watch?v=GSBLe8cKu0s


class BuildingPoint(object):
    def __init__(self, point, is_start, height):
        self.point = point
        self.is_start = is_start
        self.height = height

    def __lt__(self, other):
        # If the x coordinates of the 2 buildings are not same, just compare based on that itself.
        # We want the array to be primarily sorted based on x coordinates.
        if self.point != other.point:
            return self.point < other.point
        # EDGE CASES.
        # 1. But if x coords are same, then we need to handle some edge cases.
        # Buildings A and B start at same x coord -> Building with higher height has to come first.
        # Because we want to process and then add the higher height to the queue, and the output.
        # (Logically makes sense, it will dwarf the smaller one.)
        # 2. Buildings A and B end at same x coord -> Building with lower height has to come first,
        # we want to process this first. (The higher building should be the output.)
        # 3. Building A starts and building B ends at the same x coord -> Start should come before
        # end, or else we will add 0 to the output, which is unintended,
        # we want to add only the starting building to the output.
        else:
            if self.is_start:
                h1 = -self.height
            else:
                h1 = self.height

            if other.is_start:
                h2 = -other.height
            else:
                h2 = other.height

            return h1 < h2


class Solution:
    # Runtime: 2707 ms, faster than 10.66% of Python3 online submissions.
    # Memory Usage: 20.3 MB, less than 21.63% of Python3 online submissions.
    def getSkyline(self, buildings):
        building_points = []
        # Add all the buildings to a list, based on the x coordinate, also track start and finish.
        for building in buildings:
            building_points.append(BuildingPoint(building[0], True, building[2]))
            building_points.append(BuildingPoint(building[1], False, building[2]))
        # Sort it based on x coords, whilst handling same coords.
        building_points = sorted(building_points)

        # Keep track of all the heights, and also to get the max height at any time.
        # Not very optimal, JAVA version is logN time complexity, code is ported from there.
        queue = defaultdict(int)
        # Default min value. Never to be deleted.
        queue[0] = 1
        prev_max_height = 0
        result = []
        for building_point in building_points:
            if building_point.is_start:
                # For starts, increment count.
                queue[building_point.height] += 1
            else:
                # For ends, decrease count, or delete it.
                if queue[building_point.height] == 1:
                    del queue[building_point.height]
                else:
                    queue[building_point.height] -= 1

            # Get current max from queue.
            current_max_height = max(queue.keys())

            # If current max is not same as prev max, add point to output array.
            if prev_max_height != current_max_height:
                result.append([building_point.point, current_max_height])
                prev_max_height = current_max_height
        return result


if __name__ == "__main__":
    assert Solution.get_skyline(
        [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    ) == [
        [2, 10],
        [3, 15],
        [7, 12],
        [12, 0],
        [15, 10],
        [20, 8],
        [24, 0],
    ]
