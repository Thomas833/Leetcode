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
    
def solution(p: TreeNode, q: TreeNode)->bool:
    if not p and not q: # if both None
        return True
    if not p or not q: # if one None
        return False
    
    # check node's values now that we know they aren't None
    if p.val != q.val:
        return False
    
    #if nodes' values equal, recurse
    return solution(p.left,q.left) and solution(p.right,q.right)
    


tree1 = build_tree([1,1,3,4])
tree2 = build_tree([1,2,3,4])

print(solution(tree1, tree2))
