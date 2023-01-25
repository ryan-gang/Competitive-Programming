from typing import List


class Solution:
    # Runtime: 1206 ms, faster than 86.21%.
    # Memory Usage: 52.6 MB, less than 45.40%.
    # T : O(Nodes), S : O(Nodes)
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        """
        We traverse starting from both the nodes, and keep a track of all visited nodes and
        distance from the starting node.
        Finally we check which are the nodes reachable from both starting nodes,
        and find the node with the min distance.
        """
        visited1: dict[int, int] = {}
        visited2: dict[int, int] = {}
        dist, node = 0, node1
        while node not in visited1:
            if node == -1:
                break
            visited1[node] = dist
            node = edges[node]
            dist += 1

        dist, node = 0, node2
        while node not in visited2:
            if node == -1:
                break
            visited2[node] = dist
            node = edges[node]
            dist += 1

        v: set[int] = visited1.keys() & visited2.keys()
        distances: list[tuple[int, int]] = [
            (max(visited1[node], visited2[node]), node) for node in v
        ]
        return (min(distances)[1]) if distances else -1


if __name__ == "__main__":
    sol = Solution()
    assert sol.closestMeetingNode(edges=[2, 2, 3, -1], node1=0, node2=1) == 2
    assert sol.closestMeetingNode(edges=[1, 2, -1], node1=0, node2=2) == 2
    assert sol.closestMeetingNode(edges=[-1, -1], node1=0, node2=1) == -1
