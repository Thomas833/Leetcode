# #82 Remove Duplicates from Sorted List II - Explanation

O(n) time complexity and O(1) space complexity solution:

have dummy.next = head, tail = prev_node, and prev_node = dummy, dupe_state = False

if prev_node == dummy and head, increment tail and head

while head:
    
    if head.val == tail.val:
        dupe state true
    
    if in dupe state:
        increment head
        check if head None or head.val diff:
            if so, dupe_state = False
    assign prev_node.next = head
    tail = head
    if head:
        head = head.next

    
