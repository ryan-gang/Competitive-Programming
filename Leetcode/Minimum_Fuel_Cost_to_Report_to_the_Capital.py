from collections import defaultdict, deque
from math import ceil


class Solution:
    # Runtime: 2150 ms, faster than 43.3%.
    # Memory Usage: 62.5 MB, less than 92.40%.
    # T : O(N), S : O(N)
    def minimumFuelCost(self, roads: list[list[int]], seats: int) -> int:
        """
        We will do a BFS from the leaf nodes, to the centre, the 0th node.
        To not go backwards, or move in circles, we keep a track of the degree of each node.
        And if the degree of a neighbour is 1, only then we add neighbour to queue.
        (When we are processing node, we fetch all neighbours,
        subtract 1 from its degree, and then check if degree is equal to 1 or not.
        Logically this means, we only TRAVEL to neighbour, if this is the LAST IN EDGE to neighbour.
        Only 1 out edge is remaining (degree = 1).)
        We also keep a track of all representatives coming to a node, and then
        adding those many reps to neighbours. From this count we can find out the fuel needed.
        """
        graph: dict[int, list[int]] = defaultdict(list)  # node -> list[neighbours]
        degree: dict[int, int] = defaultdict(int)  # node -> in degree + out degree.

        for node1, node2 in roads:
            graph[node1].append(node2)
            graph[node2].append(node1)
            degree[node1] += 1
            degree[node2] += 1

        # Only add leaf nodes, to the initial queue. We start BFS from the leaves.
        queue: deque[int] = deque()
        for node in degree:
            if (degree[node]) == 1 and node != 0:
                queue.append(node)

        litres = 0
        # Store representatives, at a specific node. (Useful for keeping track subtree situations.
        # Like : 3 nodes, shipping in reps to a specific node.)
        representatives = [1] * (len(roads) + 1)

        while queue:
            # For each node. We add the fuel needed to move reps from node to the neighbour.
            # We also copy the count reps from node to neighbour.
            # But if and only if neighbour's degree is 1, we add it to queue.
            # A -> D <- B. In this case D will be added twice.
            # But if we check for degree, we can add it only once, at the appropriate time.
            node = queue.popleft()
            litres += ceil(representatives[node] / seats)

            for neighbor in graph[node]:
                degree[neighbor] -= 1
                representatives[neighbor] += representatives[node]
                if degree[neighbor] == 1 and neighbor != 0:
                    queue.append(neighbor)
        return litres


if __name__ == "__main__":
    sol = Solution()
    assert sol.minimumFuelCost(roads=[[0, 1], [0, 2], [0, 3]], seats=5) == 3
    assert sol.minimumFuelCost(roads=[[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]], seats=2) == 7
    assert sol.minimumFuelCost(roads=[], seats=1) == 0
    assert sol.minimumFuelCost(roads=[[0, 1], [0, 2], [1, 3], [1, 4]], seats=5) == 4
    assert sol.minimumFuelCost(roads=[[0, 1], [1, 2]], seats=3) == 2
