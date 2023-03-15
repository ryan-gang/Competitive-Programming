from collections import defaultdict


# Runtime: 1119 ms, faster than 15.15%.
# Memory Usage: 78 MB, less than 75.69%.
# T : O(1), S : O(N)
class LFUCache:
    """
    We can just use 2 dictionaries to implement LFU cache.
    One dict "map" to store key -> number of times it was accessed.
    Another dict "counter" frequency -> {key -> value}
    From the counter dict, we can get the keys that are used for a specific number of times.
    And remove the least frequently used keys.
    If there are mutliple such keys, we can still get the one that was used the earliest.
    Since Python3.7 dicts preserve insertion order. So we can rely on our old pal dict itself
    for the order, but in other languages we would need to implement a linked list to
    store this order.
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.used_capacity = 0
        self.least_frequency = 0
        self.map: dict[int, int] = defaultdict(int)  # Key -> used count
        self.counter: dict[int, dict[int, int]] = defaultdict(dict)  # frequency -> {key -> value}
        # Dict will preserve insertion order.

    def _increment_frequency(self, key: int, freq: int) -> int:
        """
        Increments the frequency of a pre-existing key.
        Updates the map, and the counter.
        To be used after every get and put.
        """
        new_freq = freq + 1
        val = self.counter[freq][key]
        del self.counter[freq][key]
        self.counter[new_freq][key] = val
        self.map[key] += 1
        if freq == self.least_frequency and len(self.counter[freq]) == 0:
            self.least_frequency += 1
        return new_freq

    def _insert_new_key(self, key: int, val: int) -> None:
        """
        Inserts a new key into our cache.
        If there is capacity, just add a new key, with given value and frequency = 1.
        Else, remove the least recently used key from map and counter.
        And then add the new key, value pair.
        """
        if self.used_capacity == self.capacity:
            least_used_key = next(iter(self.counter[self.least_frequency]))
            del self.counter[self.least_frequency][least_used_key]
            del self.map[least_used_key]
            self.used_capacity -= 1

        self.map[key] = 1
        self.counter[1][key] = val
        self.least_frequency = 1
        self.used_capacity += 1

    def get(self, key: int) -> int:
        if key in self.map:
            updated_freq = self._increment_frequency(key, self.map[key])
            return self.counter[updated_freq][key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            updated_freq = self._increment_frequency(key, self.map[key])
            self.counter[updated_freq][key] = value
        else:
            self._insert_new_key(key, value)


if __name__ == "__main__":
    cache = LFUCache(2)
    (cache.put(1, 1))
    (cache.put(2, 2))
    (cache.put(2, 3))
    (cache.put(4, 4))
    assert (cache.get(2)) == 3
