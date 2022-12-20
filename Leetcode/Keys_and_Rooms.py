from typing import List


class Solution:
    # Runtime: 168 ms, faster than 14.19%.
    # Memory Usage: 14.5 MB, less than 39.38%.
    # T : O(N), S : O(N)
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """Simple BFS."""
        visited = set()
        queue = [0]
        while queue:
            key = queue.pop()
            if key not in visited:
                visited.add(key)
                fetched_keys = rooms[key]
                queue.extend(fetched_keys)

        return len(visited) == len(rooms)

    def canVisitAllRoomsNice(self, rooms: List[List[int]]) -> bool:
        dfs = [0]
        seen = set(dfs)
        while dfs:
            i = dfs.pop()
            for j in rooms[i]:
                if j not in seen:
                    dfs.append(j)
                    seen.add(j)
                    if len(seen) == len(rooms):
                        return True
        return len(seen) == len(rooms)
