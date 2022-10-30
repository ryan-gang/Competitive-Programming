from typing import Dict, List


class TrieNode:
    def __init__(self, val: str = "") -> None:
        self.val = val
        self.children: Dict[str, TrieNode] = {}
        self.is_end: bool = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

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

    def printStartingWith(self, prefix: str) -> List[str]:
        self.out = []
        node = self.root
        for char in prefix:
            if char not in node.children:
                return self.out
            node = node.children[char]
        # Entire prefix has been traversed. Now print words starting from this node's children.
        self.dfs(node, [prefix])
        self.out.sort()
        return self.out

    def dfs(self, node: TrieNode, string: List[str]) -> None:
        if node.is_end:
            self.out.append("".join(string))

        for char in node.children:
            string.append(char)
            self.dfs(node.children[char], string)
            string.pop()


class Solution:
    def displayContacts(self, n, contact, s) -> List[str]:
        answer = []
        trie = Trie()
        for name in contact:
            trie.insert(word=name)
        for i in range(1, len(s) + 1):
            prefix = s[:i]

            out = trie.printStartingWith(prefix)
            if not out:
                answer.append(["0"])
            else:
                answer.append(out)

        return answer


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        contact = input().split()
        s = input()

        ob = Solution()
        ans = ob.displayContacts(n, contact, s)
        for i in range(len(s)):
            for val in ans[i]:
                print(val, end=" ")
            print()
