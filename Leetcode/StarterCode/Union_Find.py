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

    def __init__(self, L: int) -> None:
        self.parent = [-1] * L

    def find(self, node: int) -> int:
        if self.parent[node] == node:
            return node
        else:
            # path-compression-optimization
            self.parent[node] = self.find(self.parent[node])
            return self.parent[node]

    def union(self, node1: int, node2: int) -> bool:
        parent1 = self.find(node1)
        parent2 = self.find(node2)
        if parent1 != parent2:
            self.parent[parent1] = parent2
            return True
        return False

    def new(self, node: int) -> None:
        self.parent[node] = node


# Ref : https://leetcode.com/problems/number-of-islands/discuss/56354
# /1D-Union-Find-Java-solution-easily-generalized-to-other-problems

# Ref : https://cp-algorithms.com/data_structures/disjoint_set_union.html
