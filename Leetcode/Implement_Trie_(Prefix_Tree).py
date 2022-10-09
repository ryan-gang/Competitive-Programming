from typing import Dict


"""
class TrieNode:
    def __init__(self, val: Optional[str] = None) -> None:
        self.val = val
        self.children: List[TrieNode] = []


# Runtime: 6032 ms, faster than 5.01% of Python3 online submissions.
# Memory Usage: 32.4 MB, less than 18.76% of Python3 online submissions.
class Trie:
    def __init__(self):
        self.root = TrieNode("root")

    def __insert__(self, prev: TrieNode, word: str, index: int = 0) -> TrieNode:
        if index < len(word):
            char = word[index]
            # Check if current char node already exists as a child
            child_nodes = [i.val for i in prev.children]
            if char in child_nodes:
                for i in prev.children:
                    if i.val == char:
                        node = i
            else:
                node = TrieNode(char)

            node.children.append(self.__insert__(node, word, index + 1))
        else:
            node = TrieNode(None)

        prev.children.append(node)
        return node

    def insert(self, word: str) -> None:
        self.__insert__(self.root, word, 0)

    def __search__(
        self, word: str, root: TrieNode, index: int, ends_with_None: bool = False
    ) -> bool:
        if index < len(word):
            val = word[index]
            for node in root.children:
                if node.val == val:
                    return self.__search__(word, node, index + 1, ends_with_None)
        else:
            if not ends_with_None:
                return True
            else:
                for node in root.children:
                    if node.val is None:
                        return True
                return False

    def search(self, word: str) -> bool:
        return self.__search__(word, self.root, 0, True)

    def startsWith(self, prefix: str) -> bool:
        return self.__search__(prefix, self.root, 0)
"""

# Runtime: 391 ms, faster than 33.98% of Python3 online submissions.
# Memory Usage: 31.5 MB, less than 72.58% of Python3 online submissions.
"""In my self implementation, I just used a List[TrieNode] to keep track of all the
children of a node in the Trie. This was exceptionally stupid and unoptimal, using a
dictionary makes the code far more concise, and saves a lot of time; instead of
searching nodes based on their values, we can just access them from the dict.
Should have thought of this earlier. :("""


class TrieNode:
    def __init__(self, val: str = "") -> None:
        self.val = val
        self.children: Dict[str, TrieNode] = {}
        self.is_end: bool = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # T  : O(m), S : O(m) ; where m is the length of `word`
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        node.is_end = True

    # T : O(m), S : O(1) ; where m is the length of `word`
    def __search__(self, word: str, end_of_word: bool = False) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        if not end_of_word:
            return True
        else:
            return node.is_end

    def search(self, word: str) -> bool:
        return self.__search__(word, end_of_word=True)

    def startsWith(self, prefix: str) -> bool:
        return self.__search__(prefix, end_of_word=False)


if __name__ == "__main__":
    trie = Trie()
    trie.insert(word="apple")
    param_2 = trie.search(word="apple")
    param_3 = trie.startsWith(prefix="app")
