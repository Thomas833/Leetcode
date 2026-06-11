from binarytree import Node
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solution(preorder: list, inorder: list)->TreeNode   :
    hashmap = {}
    preorder = deque(preorder)

    #populate hashmap
    for i in range(len(inorder)):
        hashmap[inorder[i]] = i

    def build(start: int, end: int)->TreeNode:
        if start > end:
            return None
        root = TreeNode(preorder.popleft())
        mid = hashmap[root.val]
        root.left = build(start,mid - 1)
        root.right = build(mid + 1, end)

        return root
    return build(0, len(inorder)-1)

