from collections import deque


# Ref :
# https://leetcode.com/problems/collect-coins-in-a-tree/solutions/3342149/clear-explanation-o-n-c-code/
# https://leetcode.com/problems/collect-coins-in-a-tree/solutions/3342036/c-java-python3-trim-the-tree/
class Solution:
    def collectTheCoins(self, coins: list[int], edges: list[list[int]]) -> int:
        """
        1. First of all trim the graph. Remove all the leaves with no coins. Repeat
        this process until we get a graph with all leaves having coins. This is
        the graph that needs to be analyzed.

        2. Now since we can collect the coins from a distance of 2, We will never
        have to traverse the edges containing these leaves as a vertex. So
        transfer the coins to the parents of respective leaves and delete these
        edges.

        3. Now we have a new graph with new leaves. Here we can only collect points
        from a distance of 1. Find the number of leaves in this new graph. We
        will never have to traverse these leaves (similar logic as above).
        Remove their edges (edges containing the leaves as a vertex). This is
        the final graph that we will traverse. Every edge will be traversed
        twice (as we need to come back to the starting position as well). The
        order of traversal does not matter.
        """
        n = len(coins)
        # Create a better representation of the graph for our use.
        tree: list[set[int]] = [set() for _ in range(n)]
        for u, v in edges:
            tree[u].add(v)
            tree[v].add(u)
        print(tree)

        leaf: deque[int] = deque()
        # Now, we will prune all the leaves that are devoid of coins.
        # When we remove a leaf, we are removing the edges from itself to
        # others, but we also need to remove edges from the other nodes to this
        # leaf. And after this edge removal, the inner node might become a leaf,
        # so we need to do this recursively.
        # After this process we only have leaves that contain coins.
        for u in range(n):
            while len(tree[u]) == 1 and not coins[u]:
                v = tree[u].pop()
                tree[v].remove(u)
                u = v
            if len(tree[u]) == 1:
                # Add all leaf with coins to queue.
                leaf.append(u)

        print(tree)
        print(leaf)

        # Now we will consider the parents of the leaf nodes, as we can collect
        # the coins from here. We repeat this step twice to simulate collecting
        # coins from a distance of 2. After removing all the unnecessary nodes,
        # now we have the nodes that we HAVE to traverse. And will lead to the
        # optimal path. As we need to return to the origin, we can just return 2
        # * length of walk.
        for _ in range(2):
            for _ in range(len(leaf)):
                u = leaf.popleft()
                if tree[u]:
                    v = tree[u].pop()
                    tree[v].remove(u)
                    if len(tree[v]) == 1:
                        leaf.append(v)
            print(tree)
            print(leaf)

        return sum(len(tree[u]) for u in range(n))


if __name__ == "__main__":
    sol = Solution()
    assert (
        sol.collectTheCoins(
            coins=[0, 0, 0, 1, 1, 0, 0, 1],
            edges=[[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [5, 6], [5, 7]],
        )
        == 2
    )
