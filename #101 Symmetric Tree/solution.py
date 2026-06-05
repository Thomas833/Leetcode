from collections import deque
from binarytree import Node

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values):
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])

    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        # Left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def solution(root: TreeNode)->bool:
    if not root:
        return False
    def recurse(node1: TreeNode, node2: TreeNode)->bool:
        if ((node1 is None) != (node2 is None)): # One node is None
            return False
        elif not node1 and not node2: # Both None
            return True

        # compare values of nodes
        if (node1.val != node2.val):
            return False

        # recurse since nodes have values and they match
        return recurse(node1.left, node2.right) and recurse(node1.right, node2.left)

    return recurse(root.left,root.right)


tree = build_tree([1,2,2,3,4,4,4])

root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)
print(solution(tree))
print(root)
