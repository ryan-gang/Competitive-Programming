from collections import defaultdict
from typing import List


class Solution:
    # Runtime: 259 ms, faster than 18.43% of Python3 online submissions.
    # Memory Usage: 15.6 MB, less than 60.83% of Python3 online submissions.
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # prerequisites looks like -> [[1, 0], [2, 0], [3, 1]]; where we need to
        # complete "0" before starting "1". So we create 2 dictionaries,
        # to store the incoming and outgoing edges of our "graph".
        # After populating the dictionaries, we add all the courses that don't have any
        # prerequisites to the "order". Now from this list of courses, we see what other
        # courses have these "finished" courses as their prerequisites and then check if
        # they can be started now. The criteria of starting a course, is that it can not
        # have any dependencies remaining. In our implementation, this is in the shape of
        # the "incoming" dict which holds prerequisites. And "outgoing" which holds the
        # courses of which this course is a prerequisite.
        # So we keep on checking if we have any new course that can be finished,
        # add finish it, and then remove this from the list of prerequisites of other
        # courses. If at any point we are unable to proceed, it would mean there is a
        # circular dependency, we can return [] from there. A try catch block works just fine.

        incoming = defaultdict(list)
        outgoing = defaultdict(list)

        for i in range(numCourses):
            incoming[i] = []
            outgoing[i] = []

        for courses in prerequisites:
            post, pre = courses
            incoming[post].append(pre)
            outgoing[pre].append(post)

        # print(incoming)
        # print(outgoing)

        order = []
        idx = 0  # Index from where to start processing

        for key in incoming:
            if len(incoming[key]) == 0:
                # All courses that do not have any prerequisites can be added to order.
                order.append(key)

        while idx < numCourses:
            # Process the courses one by one,
            # By process I mean, remove the outgoing nodes, and then find children.
            if len(order) <= idx:
                return []
            course = order[idx]
            children = outgoing[course]
            for child in children:
                incoming[child].remove(course)
                if len(incoming[child]) == 0:
                    order.append(child)
            idx += 1

        return order


if __name__ == "__main__":
    sol = Solution()
    assert sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) == [0, 1, 2, 3]
    assert sol.findOrder(6, [[3, 0], [1, 5], [3, 1], [0, 5], [2, 3]]) == [4, 5, 1, 0, 3, 2]
    assert sol.findOrder(2, [[0, 1], [1, 0]]) == []
