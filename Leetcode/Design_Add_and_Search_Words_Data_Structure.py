from StarterCode.trie import TrieNode


# Runtime: 8494 ms, faster than 79.57%.
# Memory Usage: 78.1 MB, less than 51.26%.
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    # T  : O(m), S : O(m) ; where m is the length of `word`
    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        node.is_end = True

    # T : O(M), where M is the sum of lengths of all the words in our Trie.
    # For a wildcard search on "...." the dfs will visit all nodes.
    # Without any wildcard char, T : O(m), m is length of `word`.
    def __wildcard_search__(self, word: str, wildcard_char: str = ".", end_of_word: bool = True):
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
        return self.__wildcard_search__(word, wildcard_char=".", end_of_word=True)


if __name__ == "__main__":
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    assert not wd.search("pad")
    assert wd.search("bad")
    assert wd.search(".ad")
    assert wd.search("b..")
