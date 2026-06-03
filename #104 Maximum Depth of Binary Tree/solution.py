from collections import deque

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

def solution(root:TreeNode)->int:
    def recurse(node:TreeNode, depth)->int:
        if not node: # node is None
            return depth
        left = recurse(node.left, depth + 1)
        right = recurse(node.right, depth + 1)
        return max(left, right)
    
    #check if root is None
    if not root:
        return 0
    return recurse(root, 0)


   



root = build_tree([3, 9, 20, None, None, 15, 7])
print(solution(root))
