from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(
        self,
        x: int,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = x
        self.left = left
        self.right = right


def treeNodeToString(root: Optional[TreeNode]):
    if not root:
        return "[]"
    output = ""
    queue: list[Optional[TreeNode]] = [root]
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


def stringToTreeNode(input_list: list[Optional[int]]):
    if not input_list or not input_list[0]:
        return None

    root = TreeNode(int(input_list[0]))
    queue = [root]
    front = 0
    index = 1
    while index < len(input_list):
        node = queue[front]
        front = front + 1

        item = input_list[index]
        index = index + 1
        if item is not None:
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            queue.append(node.left)

        if index >= len(input_list):
            break

        item = input_list[index]
        index = index + 1
        if item is not None:
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            queue.append(node.right)
    return root


def prettyPrintTree(node: Optional[TreeNode], prefix: str = "", isLeft: bool = True):
    if not node:
        print("Empty Tree")
        return

    if node.right:
        prettyPrintTree(node.right, prefix + ("│   " if isLeft else "    "), False)

    print(prefix + ("└── " if isLeft else "┌── ") + str(node.val))

    if node.left:
        prettyPrintTree(node.left, prefix + ("    " if isLeft else "│   "), True)


# Traversals.
def inorder(node: Optional[TreeNode]):
    if node is not None:
        inorder(node.left)
        print(node.val, end=", ")
        inorder(node.right)


def preorder(node: Optional[TreeNode]):
    if node is not None:
        print(node.val, end=", ")
        preorder(node.left)
        preorder(node.right)


def postorder(node: Optional[TreeNode]):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.val, end=", ")


if __name__ == "__main__":
    tree = [1, 2, 3, 4, None, 5, 6, 7, 8, 9]
    node = stringToTreeNode(tree)
    prettyPrintTree(node)
    print("\nInorder")
    inorder(node)
