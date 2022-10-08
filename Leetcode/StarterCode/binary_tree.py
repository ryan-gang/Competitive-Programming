from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = x
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"


def stringToTreeNode(input):
    if not input:
        return None

    inputValues = [s for s in input]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def prettyPrintTree(node, prefix="", isLeft=True):
    if not node:
        print("Empty Tree")
        return

    if node.right:
        prettyPrintTree(node.right, prefix + ("│   " if isLeft else "    "), False)

    print(prefix + ("└── " if isLeft else "┌── ") + str(node.val))

    if node.left:
        prettyPrintTree(node.left, prefix + ("    " if isLeft else "│   "), True)


# Traversals.
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.val, end=", ")
        inorder(node.right)


def preorder(node):
    if node is not None:
        print(node.val, end=", ")
        preorder(node.left)
        preorder(node.right)


def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.val, end=", ")


def main():
    import sys

    def readlines():
        for line in sys.stdin:
            yield line.strip("\n")

    lines = readlines()
    while True:
        try:
            line = next(lines)
            node = stringToTreeNode(line)
            prettyPrintTree(node)
        except StopIteration:
            break


if __name__ == "__main__":
    tree = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    node = stringToTreeNode(tree)
    prettyPrintTree(node)
    print("\nInorder")
    inorder(node)
