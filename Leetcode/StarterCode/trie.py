class TrieNode:
    def __init__(self, val: str = "") -> None:
        self.val = val
        self.children: dict[str, TrieNode] = {}
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

    def __wildcard_search__(
        self, word: str, wildcard_char: str = ".", end_of_word: bool = True
    ):
        def dfs(node: TrieNode, idx: int) -> bool:
            if idx == len(word):
                if not end_of_word:
                    return True
                else:
                    return node.is_end

            char = word[idx]
            if char == wildcard_char:
                for child in node.children:
                    if dfs(node.children[child], idx + 1):
                        return True

            if char in node.children:
                return dfs(node.children[char], idx + 1)

            return False

        return dfs(self.root, idx=0)

    def search(self, word: str) -> bool:
        return self.__search__(word, end_of_word=True)

    def startsWith(self, prefix: str) -> bool:
        return self.__search__(prefix, end_of_word=False)

    def wildcard_search(self, word: str) -> bool:
        return self.__wildcard_search__(word, wildcard_char=".", end_of_word=True)

    def wildcard_starts_with(self, prefix: str) -> bool:
        return self.__wildcard_search__(prefix, wildcard_char=".", end_of_word=False)


if __name__ == "__main__":
    trie = Trie()
    trie.insert(word="bad")
    trie.insert(word="dad")
    trie.insert(word="mad")
    print(trie.search(word="pad"))  # False
    print(trie.startsWith(prefix="ma"))  # True
    print(trie.wildcard_search(word=".ad"))  # True
    print(trie.wildcard_search(word="b.."))  # True
    print(trie.wildcard_starts_with(prefix="b.."))  # True
