import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from helper_classes import linked_list_helpers as ll

def solution(head: ll.ListNode)->None:
    dummy = ll.ListNode(0,head)
    tail = dummy
    dupe_state = False

    # iterate through linked list
    while head:
        # check if tail is dummy
        if tail == dummy:
            tail = tail.next
            head = head.next
            continue
        # check if tail.val and head.val equal each other. if so, dupe state
        if tail.val == head.val:
            dupe_state = True
        # while in a dupe_state, increment head
        while dupe_state:
            head = head.next
            if not head or head.val != tail.val: # end dupe state if head.val is different or if at end of linked list
                dupe_state = False
        # set tail to head to bypass redundant values
        tail.next = head
        tail = head
        if head:
            head = head.next
    return dummy.next

l = ll.build_linked_list([1,2,2,3,3,4,4,4,4,5])
solution(l)
ll.print_linked_list(l)
