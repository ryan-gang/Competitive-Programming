from collections import deque, defaultdict
from typing import Optional

from Leetcode.StarterCode.binary_tree import TreeNode


class Solution:
    # Create an equivalent graph, to travel both forwards and backwards,
    # then simple BFS.
    # T : O(N), S : O(N).
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        graph: dict[int, list[int]] = defaultdict(list)

        # Recursively build the undirected graph from the given binary tree.
        def build_graph(cur: TreeNode, parent: Optional[TreeNode]):
            if cur and parent:
                graph[cur.val].append(parent.val)
                graph[parent.val].append(cur.val)
            if cur.left:
                build_graph(cur.left, cur)
            if cur.right:
                build_graph(cur.right, cur)

        build_graph(root, None)

        answer = []
        visited: set[int] = {target.val}

        # Add the target node to the queue with a distance of 0
        queue = deque([(target.val, 0)])
        while queue:
            curr, distance = queue.popleft()

            # If the current node is at distance k from target,
            # add it to the answer list and continue to the next node.
            if distance == k:
                answer.append(curr)
                continue

            # Add all unvisited neighbors of the current node to the queue.
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))

        return answer

# ToDo : https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/solutions/
#  143798/1ms-beat-100-simple-java-dfs-with-without-hashmap-including-explanation/.
