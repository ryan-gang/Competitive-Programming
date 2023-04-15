"""
Disjoint Set Union / Union Find.

Given several elements, each of which is a separate set. A DSU will have an
operation to combine any two sets, and it will be able to tell in which set a
specific element is.

Operations :
new(v) - creates a new set consisting of the new element `v`.
union(a, b) - merges the two specified sets (the set in which the element a is
located, and the set in which the element b is located)
find(v) - returns the representative of the set that contains the element v.
This representative is an element of its corresponding set. It is selected in
each set by the data structure itself (and can change over time, namely after
union_sets calls). This representative can be used to check if two elements are
part of the same set or not. a and b are exactly in the same set, if find(a) ==
find(b). DSU allows us to do each of these operations in almost O(1) time on
average.

Minimal example :
def validPath(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    # Check if source and destination are connected in a bidirectional graph.
    uf = Union(n)
    for v1, v2 in edges:
        if not uf.exists(v1):
            uf.new(v1)
        if not uf.exists(v2):
            uf.new(v2)
        uf.union(v1, v2)
    return uf.find(source) == uf.find(destination)
"""


class Union:
    """
    DSU data structure. (With Path Compression Optimization)
    `parent` is an array, of size `L`, where we keep track of
    all relationships between the disjoint sets.
    Just keeping track of the parent of each of the node is enough.
    `find(node)` can be used to find the `parent` of a particular node.
    `union(n1, n2)` can be used to union 2 sets, if they are disjoint.
    Returns True if union is done, else False.
    `new(node)` can be used to add a new node to the `parent` array.

    If we combine both optimizations - path compression with union by size /
    rank - we will reach nearly constant time queries. The final amortized time
    complexity is O(alpha(n)), where alpha(n) is the inverse Ackermann function,
    which grows very slowly. In fact it grows so slowly, that it doesn't exceed
    4 for all reasonable n (approximately n < 10^600).
    T : O(1) (Amortized).

    With only union-by-size optimization, T : O(logN).
    """

    DEFAULT_VALUE = -1

    def __init__(self, L: int) -> None:
        """
        Initializes the parent array, used to keep track of parents of each node.
        """
        self.parent = [self.DEFAULT_VALUE] * L
        self.size = [0] * L

    def find(self, node: int) -> int:
        """
        Returns the parent of the param node.
        While initialization all nodes are their own parents.
        path-compression-optimization :
            When the tree becomes especially long, `find(n)` can take O(N) time.
            So to make it faster ; while finding out the actual parent of n, we
            find out the parent of all nodes in the path from n to parent. And
            we set all of these nodes' parent directly to the `parent` node. Making
            the graph flatter.
        """
        if self.parent[node] == node:
            return node
        else:
            self.parent[node] = self.find(self.parent[node])  # path-compression
            return self.parent[node]

    def union(self, node1: int, node2: int) -> bool:
        """
        Find out the parents of 2 nodes.
        And if they are not the same, make them point to any one of them,
        so as to make the nodes have the same parent.
        returns True/False based on if union was successful or not.
        union-by-size/rank :
            Instead of always attaching the 2nd tree to the 1st one, which can lead to long chains.
            We use the size / rank of the trees while deciding which one to attach to.
            And then attach the one with the lower rank to the one with the bigger rank.
        """
        parent1 = self.find(node1)
        parent2 = self.find(node2)
        if parent1 != parent2:
            if self.size[parent1] < self.size[parent2]:  # union-by-size
                parent1, parent2 = parent2, parent1
            self.parent[parent2] = parent1  # parent2 is always the lower size tree here.
            self.size[parent1] += self.size[parent2]
            return True
        return False

    def exists(self, node: int) -> bool:
        """
        Check if a node is created or not.
        """
        return self.parent[node] != self.DEFAULT_VALUE

    def new(self, node: int) -> None:
        """
        Create a node.
        """
        self.parent[node] = node
        self.size[node] = 1
