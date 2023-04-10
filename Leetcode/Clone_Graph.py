from collections import deque
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, neighbors: Optional[list["Node"]] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    # Runtime: 41 ms, faster than 50.47%.
    # Memory Usage: 14.5 MB, less than 16.46%.
    # T : O(E+V), S : O(V) ; where E is edges, and V is vertices.
    def cloneGraph(self, node: "Node") -> "Node":
        """
        For each node we create a deep copy, and store it in a dict. For easy
        access via node.val -> node mapping. Then for each neighbor also we
        create deep copies and add them to the parent node's list using the
        reference in the dict.
        """
        if not node:
            return node
        q = deque([node])  # queue for bfs
        clones: dict[int, Node] = {node.val: Node(node.val, [])}  # keep a mapping of val -> Node
        seen: set[Node] = set()  # we visit every parent node only once
        while q:
            parent = q.popleft()

            for nbr in parent.neighbors:
                if parent not in seen:
                    # If we have seen parent before, no need to visit all its neighbors again.
                    q.append(nbr)
                    if nbr.val not in clones:
                        clones[nbr.val] = Node(nbr.val, [])
                        # If node not present in dict, create a new entry for it.
                    clones[parent.val].neighbors.append(clones[nbr.val])
                    # Add that entry to the parent node's neighbor list in the dict.
            seen.add(parent)

        return clones[node.val]
