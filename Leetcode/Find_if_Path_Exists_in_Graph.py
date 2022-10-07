from collections import defaultdict, deque
from typing import List, Set


# Ref : https://leetcode.com/problems/find-if-path-exists-in-graph/
# discuss/2673635/Bidirectional-Search-in-Python
class Solution:
    # Runtime: 4157 ms, faster than 29.57% of Python3 online submissions.
    # Memory Usage: 106.4 MB, less than 58.30% of Python3 online submissions.
    # T : O(k^d), S : O(k^(d-1))
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.graph: defaultdict[int, List[int]] = defaultdict(list)

        for start, end in edges:
            self.graph[start].append(end)
            self.graph[end].append(start)

        def bfs(src: int, dst: int):
            queue = deque([src])
            visited: List[int] = []
            while queue:
                node = queue.popleft()
                if node in visited:
                    continue
                if node == dst:
                    return True
                queue.extend(self.graph[node])
                visited.append(node)
            return False

        return bfs(source, destination)

    # Runtime: 3745 ms, faster than 44.97% of Python3 online submissions.
    # Memory Usage: 106.5 MB, less than 39.90% of Python3 online submissions.
    def validPathBidirectionalEachNodeAtATime(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        self.graph: defaultdict[int, List[int]] = defaultdict(list)

        for start, end in edges:
            self.graph[start].append(end)
            self.graph[end].append(start)

        def bfs(src: int, dst: int):
            queue_src = deque([src])
            queue_dst = deque([dst])
            visited_src: set[int] = set()
            visited_dst: set[int] = set()

            while queue_src or queue_dst:
                if queue_src:
                    node = queue_src.popleft()
                    if node in visited_src:
                        continue
                    queue_src.extend(self.graph[node])
                    visited_src.add(node)

                if queue_dst:
                    node = queue_dst.popleft()
                    if node in visited_dst:
                        continue
                    queue_dst.extend(self.graph[node])
                    visited_dst.add(node)

                # If there is any common visited node, between visited_dst and visited_src,
                # it means there is an available path from src to dst.
                if visited_dst.intersection(visited_src):
                    return True
            return False

        return bfs(source, destination)

    # Runtime: 3745 ms, faster than 44.97% of Python3 online submissions.
    # Memory Usage: 106.5 MB, less than 39.90% of Python3 online submissions.
    # T : O(k^(d/2)), S : O(k^(d/2))
    def validPathBidirectional(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        """
        We start BFS from both source and destination, if both the searches reach a common node,
        we can say that there is a path from source to destination.
        This implementation, traverses a layer at a time, from both sides.

        If we run BFS only from source, till destination.
        We will traverse ~(k^d) nodes.
        But if we run BFS from both source and destination.
        We will traverse (k^d/2) + (k^d/2) nodes.

        (If we assume, each node has k children, and the distance between the source and
        destination is d nodes.)

        That's a time saving in the order of O(k^d/2), at the expense of some additional
        O(k^d/2) space."""

        self.graph: defaultdict[int, List[int]] = defaultdict(list)

        for start, end in edges:
            self.graph[start].append(end)
            self.graph[end].append(start)

        def bfs_bidirection(src: int, dst: int):
            queue_src = deque([src])
            queue_dst = deque([dst])
            visited_src: Set[int] = set()
            visited_dst: Set[int] = set()

            while queue_src or queue_dst:
                # Nodes from the next layer from current layer nodes.
                queue_src_tmp: List[int] = []
                queue_dst_tmp: List[int] = []

                # We iterate over all the nodes in our current layer, adding them to the
                # visited set, and for every node, we put their children into a seperate list.
                # In this while loop, we go over all the nodes in the current layer only.
                while queue_src:
                    node = queue_src.popleft()
                    if node in visited_src:
                        continue
                    queue_src_tmp.extend(self.graph[node])
                    visited_src.add(node)

                while queue_dst:
                    node = queue_dst.popleft()
                    if node in visited_dst:
                        continue
                    queue_dst_tmp.extend(self.graph[node])
                    visited_dst.add(node)

                # After the while loops are terminated, we can add the next layer nodes to
                # the queue_src, and queue_dst, to be processed in the next iteration.
                queue_src.extend(queue_src_tmp)
                queue_dst.extend(queue_dst_tmp)

                # If there is any common visited node, between visited_dst and visited_src,
                # it means there is an available path from src to dst.
                # From src we have reached ---> X
                # From dst also we have reached ---> X
                # It follows that we can reach from src to dst following the same paths.
                if visited_dst.intersection(visited_src):
                    return True

            return False

        return bfs_bidirection(source, destination)


if __name__ == "__main__":
    sol = Solution()
    assert sol.validPathBidirectional(n=3, edges=[[0, 1], [1, 2], [2, 0]], source=0, destination=2)
    assert not sol.validPathBidirectional(
        n=6, edges=[[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], source=0, destination=5
    )
