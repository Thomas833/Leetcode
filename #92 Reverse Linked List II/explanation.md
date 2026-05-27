# #92 Reverse Linked List II - Explanation

have counter initialized to 1 on the head of the list. If counter less than left, simply set head to head.next. have a tail pointer to stop on the node before the reversing. have an end pointer to point to node that breaks the reverse while loop

if counter == left, then we go into a while loop that stops when the counter is greater than right
in this while loop, put each node in a stack. once the loop breaks, go into another loop to then set the tail's pointer to the top node, pop it, and increment the tail to tail.next. continue until stack is empty. once done, set the tail pointer to the end node

Time complexity is O(n + k + k) where k is the size of the reversed stack. Space complexity is O(k)