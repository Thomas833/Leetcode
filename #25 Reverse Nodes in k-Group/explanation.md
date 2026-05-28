# #25 Reverse Nodes in k-Group - Explanation

add nodes to stack until counter = k. loop through stack and set the top node.next to next node and set tail.next to that node. reset counter and begin with next node. end outer while loop when node you would start reversing with is None

time and space complexity O(2n) becomes O(n) because each node is appended to and popped from stack and we walk through the linked list once. 

          h
1 -> 2 -> 3, k = 2


2 -> 1
head = 3
linkNode =  1
stack = []
counter = 1
original = 2
populatedNode = 1


append nodes to stack while counter not greater than k. iterate with head

if linkNode is None, meaning in first k-group, set original to first popped node. if linkNode has value, set to popped node
when popping, set linkNode to popped node. when stack empty, last node set will be linkNode.

reset counter



There is set reversal algorithm for linked lists. the efficient solutions show how its done and simply stop at a specific node rather than None

