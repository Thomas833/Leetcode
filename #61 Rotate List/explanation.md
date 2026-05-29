# #61 Rotate List - Explanation

pointers:
dummy: points to head of list
tail: equals dummy until counter > k

counter = 1

walk along linked list to get length
if k > counter, reduce with mod

walk through list until head at end, but this time increment tail when counter > k

with pointers in place, point head, which is at end node of list, to dummy.next, which is pointing to the head node. tail is on the new end node, so set dummy.next to tail.next and then set tail.next to None. return dummy.next

O(n + n) -> O(n) time complexity and O(1) space complexity
