class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def solution():
    

    def findSum(root: TreeNode, targetSum: int)->bool:
        if not root:
            return False

        def recurse(node: TreeNode, total: int)->bool:
            total += node.val
            if not node.left and not node.right: # both are None
                if total == targetSum:
                    return True
                else:
                    return False
            else: # keep going down tree until reach leaf node
                if node.left:
                    left = recurse(node.left, total)
                else:
                    left = False
                if node.right:
                    right = recurse(node.right, total)
                else:
                    right = False
            return left or right
        return recurse(root,0)

#EFFICIENT SOLUTION:
def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root is None:
            return False
        if root.left == None and root.right == None:
            return targetSum == root.val

        return (self.hasPathSum(root.left, targetSum - root.val)) or (self.hasPathSum(root.right, targetSum - root.val))
