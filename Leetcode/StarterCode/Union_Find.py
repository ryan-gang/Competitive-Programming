class Union:
    """
    DSU data structure. (With Path Compression Optimization)
    parent is an array, of size L, where we keep track of
    all relationships between the disjoint sets.
    find(node) can be used to find the parent of a particular node.
    union(n1, n2) can be used to union 2 nodes, if they are disjoint.
    Returns True if union is done, else False.
    new(node) can be used to add a new node to the parent array.
    """

    DEFAULT = -1

    def __init__(self, L: int) -> None:
        """
        Initializes the parent array, used to keep track of parents of each node.
        Very easy way to represent a DSU DS.
        """
        self.parent = [Union.DEFAULT] * L

    def find(self, node: int) -> int:
        """
        Returns the parent of the param node.
        While initializing all nodes are their own parents.
        """
        if self.parent[node] == node:
            return node
        else:
            # path-compression-optimization
            self.parent[node] = self.find(self.parent[node])
            return self.parent[node]

    def union(self, node1: int, node2: int) -> bool:
        """
        Find out the parents of 2 nodes.
        And if they are not the same, make them point to any one of them,
        so as to make the nodes have the same parent.
        """
        parent1 = self.find(node1)
        parent2 = self.find(node2)
        if parent1 != parent2:
            self.parent[parent1] = parent2
            return True
        return False

    def exists(self, node: int) -> bool:
        """
        Check if a node is created or not.
        """
        return self.parent[node] != Union.DEFAULT

    def new(self, node: int) -> None:
        """
        Create a node.
        """
        self.parent[node] = node


# Ref : https://leetcode.com/problems/number-of-islands/discuss/56354
# /1D-Union-Find-Java-solution-easily-generalized-to-other-problems

# Ref : https://cp-algorithms.com/data_structures/disjoint_set_union.html
