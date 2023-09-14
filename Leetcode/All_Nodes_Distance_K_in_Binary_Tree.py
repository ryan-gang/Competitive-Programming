from collections import deque, defaultdict
from typing import Optional
from Leetcode.StarterCode.Binary_Tree import TreeNode


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

        answer: list[int] = []
        visited: set[int] = {target.val}

        # Add the target node to the queue with a distance of 0
        queue: deque[tuple[int, int]] = deque([(target.val, 0)])
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

    """
    Add child -> parent mappings.
    Then do BFS from target node, until k hops.
    """
    # T : O(N), S : O(N), where N is total number of nodes.
    def distanceK1(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        mapping: dict[TreeNode, TreeNode] = {}  # Child -> Parent mapping.
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if left_child := node.left:
                mapping[left_child] = node
                queue.append(left_child)
            if right_child := node.right:
                mapping[right_child] = node
                queue.append(right_child)

        queue = deque([target])
        seen = set([target])
        # Seen so that we don't go back to the node where we came from.
        while k:
            for _ in range(len(queue)):  # All nodes @ current distance
                node = queue.popleft()
                for child in [node.left, node.right, mapping.get(node)]:
                    if child and child not in seen:
                        seen.add(child)
                        queue.append((child))
            k -= 1
        return [node.val for node in queue]
