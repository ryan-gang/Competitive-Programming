from StarterCode.disjoint_set_union import Union
from collections import defaultdict, deque


class Solution:
    """
    Simple BFS.
    Traverse from src to dst, only through edges with weight strictly less than
    the limit.
    But, due to visiting each edge multiple times, for individual queries, this
    leads to TLE. We need to somehow remove this repeated work.
    """

    def distanceLimitedPathsExistTLE(
        self, n: int, edgeList: list[list[int]], queries: list[list[int]]
    ) -> list[bool]:
        g: dict[int, set[int]] = defaultdict(set)  # node -> node mapping
        d: dict[str, int] = {}  # min edge distance
        for u, v, dis in edgeList:
            g[u].add(v)
            g[v].add(u)
            key = str(sorted([u, v]))
            if key not in d:
                d[key] = dis
            else:
                d[key] = min(d[key], dis)

        out: list[bool] = []

        def search(src: int, dst: int, max_dis: int) -> bool:
            q = deque([src])
            seen: set[int] = set()
            while q:
                node = q.popleft()
                if node == dst:
                    return True
                for child in g[node]:
                    key = str(sorted([node, child]))
                    if d[key] < max_dis and child not in seen:
                        q.append(child)
                        seen.add(child)

            return False

        for src, dst, max_dis in queries:
            out.append(search(src, dst, max_dis))

        return out

    """
    We start by sorting both the queries, and edges on the basis of the weights
    of edges. Then we keep on union-ing nodes in order, as long as they are less
    than the limit of the current query. So, for a query `q` with limit = L. We
    union all nodes joined by edges less than L. If the src and dst for `q` are
    in the same set, we return True, else False. And then keep on doing the same
    thing for the rest of the nodes. But now we have the old nodes already
    processed (upto limit = L).
    """
    # T : O(N + ELogE + QLogQ + Alpha(N) * (E+Q)), S : O(N + Q)
    def distanceLimitedPathsExist(
        self, n: int, edge_list_: list[list[int]], queries_: list[list[int]]
    ) -> list[bool]:
        edge_list: list[tuple[int, int, int]] = sorted(
            ((u, v, dis) for u, v, dis in edge_list_), key=lambda x: x[2]
        )
        queries: list[tuple[int, int, int, int]] = sorted(
            ((p, q, lim, idx) for idx, (p, q, lim) in enumerate(queries_)), key=lambda x: x[2]
        )

        uf = Union(n)
        for i in range(n):
            uf.new(i)
        idx = 0
        out = [False] * len(queries)
        for p, q, limit, i in queries:
            while idx < len(edge_list) and edge_list[idx][2] < limit:
                node1, node2 = edge_list[idx][0], edge_list[idx][1]
                uf.union(node1, node2)
                idx += 1
            out[i] = uf.find(p) == uf.find(q) and uf.find(p) != -1

        return out


if __name__ == "__main__":
    sol = Solution()
    assert sol.distanceLimitedPathsExist(
        n=3,
        edge_list_=[[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]],
        queries_=[[0, 1, 2], [0, 2, 5]],
    ) == [False, True]
    assert sol.distanceLimitedPathsExist(
        n=5,
        edge_list_=[[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]],
        queries_=[[0, 4, 14], [1, 4, 13]],
    ) == [True, False]
