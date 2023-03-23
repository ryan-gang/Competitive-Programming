from StarterCode.Union_Find import Union


class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        uf = Union(n)
        # For all the nodes in our network, create corresponding nodes in our
        # data structure.
        for _ in range(n):
            uf.new(_)

        redundant = 0
        # For all the connections, we check if both the nodes are already
        # connected or not, if they are already connected, the connection is
        # redundant and can be used somewhere else.
        for v1, v2 in connections:
            if uf.find(v1) != uf.find(v2):
                uf.union(v1, v2)
            else:
                redundant += 1

        roots = 0
        # Now we scan all the nodes, and see how many "root"s are there. Our
        # network would have 1 root, but there also could be disjoint nodes
        # which will show up as their own roots.
        for node in range(n):
            if uf.find(node) == node:
                roots += 1

        disjoint_nodes = roots - 1
        # We can join N disjoint nodes, within themselves using N - 1
        # connections. And 1 more connection to join that secondary network to
        # the primary one. So, we need N connections to join N disjoint nodes to
        # our main network. If we have more redundant connections than our
        # disjoint nodes, we can connect all of them, using only
        # min(disjoint_nodes, redundant) connections. But if we don't have as
        # many redundant connections we can't finish the entire thing.
        if disjoint_nodes <= redundant:
            return disjoint_nodes
        else:
            return -1


if __name__ == "__main__":
    sol = Solution()
    assert sol.makeConnected(n=4, connections=[[0, 1], [0, 2], [1, 2]]) == 1
    assert sol.makeConnected(n=6, connections=[[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]) == 2
    assert sol.makeConnected(n=6, connections=[[0, 1], [0, 2], [0, 3], [1, 2]]) == -1
