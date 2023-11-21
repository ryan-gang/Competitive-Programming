class Solution:
    # T : O(M * N), S : O(1)
    # Where M is types of garbage and N is len(garbage)
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        travel.append(0)  # This value won't be used, just accessed by unused
        total = 0

        for type in ["P", "G", "M"]:
            unused = 0
            for idx, val in enumerate(garbage):
                if type in val:
                    # Unused is the distance traveled by the truck from the last
                    # time this type of garbage was seen to current index. If
                    # this type of garbage is not seen again we won't travel the
                    # distance from here on out.
                    total += unused
                    unused = travel[idx]  # reset unused
                    total += val.count(type)
                else:
                    # Update unused
                    unused += travel[idx]
        return total

    # T : O(M * N), S : O(1)
    # Where M is types of garbage and N is len(garbage)
    def garbageCollection1(self, garbage: list[str], travel: list[int]) -> int:
        # Similar logic, just we keep the types of garbage and their unused
        # distances in a dict.
        travel.append(0)
        total = 0
        distance = {"P": 0, "G": 0, "M": 0}

        for idx, curr in enumerate(garbage):
            for garbage_type in distance:
                if garbage_type in curr:
                    total += curr.count(garbage_type)
                    total += distance[garbage_type]
                    distance[garbage_type] = travel[idx]
                else:
                    distance[garbage_type] += travel[idx]

        return total

    # T : O(M * N), S : O(1)
    # Where M is types of garbage and N is len(garbage)
    def garbageCollection2(self, garbage: list[str], travel: list[int]) -> int:
        # Here we traverse from the end to the beginning, so we don't need the unused variable.
        # Once we have seen a garbage type, after that all of the distances are added.
        travel.append(0)
        total = 0
        seen = {"P": False, "G": False, "M": False}

        for i in range(len(garbage) - 1, -1, -1):
            curr = garbage[i]
            for garbage_type in seen:
                if garbage_type in curr:
                    seen[garbage_type] |= True
                if seen[garbage_type]:
                    total += curr.count(garbage_type)
                    total += travel[i - 1]

        return total
