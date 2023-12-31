from collections import defaultdict, deque
from StarterCode.Union_Find import Union


class Solution:
    # Runtime: 4157 ms, faster than 29.57% of Python3 online submissions.
    # Memory Usage: 106.4 MB, less than 58.30% of Python3 online submissions.
    # T : O(k^d), S : O(k^(d-1))
    # Unidirectional Bread First Search.
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        self.graph: defaultdict[int, list[int]] = defaultdict(list)

        for start, end in edges:
            self.graph[start].append(end)
            self.graph[end].append(start)

        def bfs(src: int, dst: int):
            queue = deque([src])
            visited: set[int] = set()
            while queue:
                node = queue.popleft()
                if node in visited:
                    continue
                if node == dst:
                    return True
                queue.extend(self.graph[node])
                visited.add(node)
            return False

        return bfs(source, destination)

    # Runtime: 3745 ms, faster than 44.97% of Python3 online submissions.
    # Memory Usage: 106.5 MB, less than 39.90% of Python3 online submissions.
    # Bidirectional Bread First Search.
    def validPath1(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        self.graph: defaultdict[int, list[int]] = defaultdict(list)

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
    # Bidirectional Bread First Search.
    def validPath2(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        """
        We start BFS from both source and destination,
        if both the searches reach a common node,
        we can say that there is a path from source to destination.
        This implementation, traverses a layer at a time, from both sides.
        If we run BFS only from source, till destination.
        We will traverse ~(k^d) nodes.
        But if we run BFS from both source and destination.
        We will traverse (k^d/2) + (k^d/2) nodes.
        (Where, each node has k children, and the distance between the source and
        destination is d nodes.)
        That's a time saving in the order of O(k^d/2), at the expense of some additional
        O(k^d/2) space.
        """
        self.graph: defaultdict[int, list[int]] = defaultdict(list)

        for start, end in edges:
            self.graph[start].append(end)
            self.graph[end].append(start)

        def bfs_bidirection(src: int, dst: int):
            queue_src = deque([src])
            queue_dst = deque([dst])
            visited_src: set[int] = set()
            visited_dst: set[int] = set()

            while queue_src or queue_dst:
                # Nodes from the next layer from current layer nodes.
                queue_src_tmp: list[int] = []
                queue_dst_tmp: list[int] = []

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

    # Runtime: 4669 ms, faster than 26.95%.
    # Memory Usage: 103.6 MB, less than 90.52%.
    # T : O(?), S : O(N) ; Time Complexity is O(m.alpha(n)),
    # where alpha is the Inverse Ackermann Function.
    # Union Find Solution.
    def validPath3(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        """
        Using Union Find to solve the question.
        Every node is added as a node in our DSU.
        And for every edge, between them the two nodes are joint together.
        Finally we check if the source and destination are joint or not.
        """
        uf = Union(n)
        for v1, v2 in edges:
            if not uf.exists(v1):
                uf.new(v1)
            if not uf.exists(v2):
                uf.new(v2)
            uf.union(v1, v2)

        return uf.find(source) == uf.find(destination)


if __name__ == "__main__":
    sol = Solution()
    assert sol.validPath(n=3, edges=[[0, 1], [1, 2], [2, 0]], source=0, destination=2)
    assert not sol.validPath(
        n=6, edges=[[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], source=0, destination=5
    )
    assert not sol.validPath(
        n=10,
        edges=[[2, 9], [7, 8], [5, 9], [7, 2], [3, 8], [2, 8], [1, 6], [3, 0], [7, 0], [8, 5]],
        source=1,
        destination=0,
    )
