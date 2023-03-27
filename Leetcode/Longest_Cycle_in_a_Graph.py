from collections import defaultdict


class Solution:
    """
    TLE.
    The logic is correct, but having a dfs specific list, where I need to
    use .index() O(N) is a drag, again having to union this with the external
    `seen` set is another major drag O(N). So, in the next solution we improve
    this by having a dfs specific dict, from where we can get the distance
    between 2 nodes, and a external seen boolean array, which is passed to dfs,
    and updated at every node.
    """

    def longestCycle(self, edges: list[int]) -> int:
        out_d: dict[int, int] = defaultdict(int)
        in_d: dict[int, list[int]] = defaultdict(list)

        for src, dst in enumerate(edges):
            out_d[src] = dst
            in_d[dst].append(src)

        def dfs(node: int, seen: list[int]) -> tuple[int, list[int]]:
            if node in seen:
                print("cycle :", seen, node)
                index = seen.index(node)
                return len(seen) - index, seen
            if node not in in_d:
                return 0, seen
            else:
                seen.append(node)
                if node in out_d:
                    return dfs(out_d[node], seen)
                else:
                    return 0, seen

        n = len(edges)
        seen: set[int] = set()
        max_cycle_length = -1
        for node in range(n):
            print(node)
            if (
                node in in_d and node not in seen
            ):  # If a node has no incoming edge, it can't form a cycle.
                cycle_length, cycle_members = dfs(node, list())
                if cycle_length > 0:
                    seen = seen.union(cycle_members)
                    max_cycle_length = max(cycle_length, max_cycle_length)

        print("max:", max_cycle_length)
        return max_cycle_length

    # Runtime: 1307 ms, faster than 73.87%.
    # Memory Usage: 135.6 MB, less than 57.10%.
    # T : O(N), S : O(N)
    def longestCycle1(self, edges: list[int]) -> int:
        """
        The problem specifies that each node has no more than one outgoing edge.
        1. Let us consider a node `node` which belongs to a cycle. It would
           imply that the only outgoing edge of `node` would also be in this
           cycle. As a result, `node` cannot be a part of any other cycle
           because it only has one outgoing edge, which is consumed in this
           cycle. This demonstrates that in a graph with only one outgoing edge,
           a node cannot be a part of more than one cycle.
        2. We would visit all the nodes in the cycle if we started a graph
           traversal from any node in the cycle. There is no point in revisiting
           the nodes in the cycle because they cannot be part of any other
           cycle.
        3. Also, there is also no point in visiting the nodes that do not form a
           cycle again. We would have iterated over the only outgoing edge (if
           they have) during the first visit and there is no point in iterating
           over it again.
        This implies that visiting each node only once is sufficient. We start a
        dfs from each unvisited node, and iterate over every outgoing edge to
        going to its neighbors, as long this the neighbor is not visited, we
        keep on traversing. If we come across a node already present in the
        internal dict, we can assume we have a cycle and calculate the length.
        The dfs specific dict is used to keep track of distance of each node
        from the starting node. And if we have a cycle, we can find out its
        length by simply doing dist[node] - dist[neighbor] + 1, where neighbor
        is the next node, and also the "start" of the cycle.
        """
        answer = -1
        n = len(edges)
        visited: list[bool] = [False] * n

        def dfs(node: int, distances: dict[int, int], visited: list[bool], edges: list[int]):
            visited[node] = True
            neighbor = edges[node]

            if neighbor != -1 and not visited[neighbor]:
                distances[neighbor] = distances[node] + 1
                dfs(neighbor, distances, visited, edges)

            elif neighbor in distances:
                cycle_length = distances[node] - distances[neighbor] + 1
                nonlocal answer
                answer = max(answer, cycle_length)

        for node in range(n):
            if not visited[node]:
                distances = {node: 1}
                dfs(node, distances, visited, edges)
        return answer


if __name__ == "__main__":
    sol = Solution()
    assert (sol.longestCycle(edges=[4, 3, 3, 4, 7, 2, 3, 3])) == 3
    assert (sol.longestCycle1(edges=[3, 3, 4, 2, 3])) == 3
    assert (sol.longestCycle1(edges=[2, -1, 3, 1])) == -1
