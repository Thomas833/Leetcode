# #101 Symmetric Tree - Explanation

given a root node exists, call a inner recursive function with the parameters being the left and right child of root

node1 represents left subtree, node2 represents right subtree
in recursive function (node 1, node 2):
    check if one or both of the nodes are None.
        if one is None, return False. If both, return True, else continue
    check the values of node 1 and node 2. if they match, continue, else return False
    -
    call the recursive function again twice. check(node1.left,node2.right), check(node1.right,node2.left)
    
