# #19 Remove n-th Node from End of List - Explanation

have a dummy node point to the head of the list. this will simplify things if the head of the list needs to be removed.

More than one pass:
have a counter increment through the list. This will give us the length of the linked list, which we then can use n to walk through the list again and change the .next field of the n-1 node to node.next = node.next.next

One pass:

Example: n = 5, dummy -> 1 -> 3 -> 4 -> 5 -> 7
dummy = ListNode(0)
dummy.next = head
forward = head
prev_node = dummy
counter = 1

head and foward and prev_node will increment while dummy holds head of linked list

iterate over linked list with pointer foward from head while counter < n. walk through list with forward only

then, iterate through list with all pointers prev_node, forward, and head. when forward.next is None, stop iterating 

set prev_node.next equal to head.next because head is node we want removed. 



