from bisect import bisect_left


class SnapshotArray:
    # Only get() is O(LogN) time, rest all are O(1) time complexity.
    # Space is O(N)
    def __init__(self, length: int):
        self.snap_id = 0
        # We can't store the entire array's state while taking a snap.
        # So, for every index we keep a track of all it's updates.
        # And then while finding a value for a given snap, we can just binary search for that snap.
        # for every index -> {snap_id : value}
        self.array: list[dict[int, int]] = [{0: 0} for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self.array[index][self.snap_id] = val

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        # If there is no updates for a given index, means the index still holds
        # it's original zero value. Return 0 in that case.
        if not self.array[index]:
            return 0
        snaps = list(self.array[index].keys())  # List of all snaps, to binary search on.
        idx = bisect_left(snaps, snap_id)  # The snap index we require.
        if idx >= len(snaps) or snaps[idx] != snap_id:
            # But as we don't store the snap_ids for every version, we need to
            # handle the situation where an id is present and absent seperately.
            # In this case the snap_id doesn't exist, so we go with the last one present.
            return self.array[index][snaps[idx - 1]]
        else:
            # If the required snap_id is present, just return the value.
            return self.array[index][snaps[idx]]
