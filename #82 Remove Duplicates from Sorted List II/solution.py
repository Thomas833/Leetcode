import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper_classes import linked_list_helpers as llh
   

def solution(head: llh.ListNode)->llh.ListNode:
    dummy = llh.ListNode(0,head)
    tail = dummy
    prev_node = dummy
    dupe_state = False

    # outer incrementation loop
    while head:
        #check if tail equal dummy
        if tail == dummy:
            tail = tail.next
            head = head.next
            continue
        
        # check for dupe state
        if tail.val == head.val:
            dupe_state = True

        # if in dupe state, move head forward until reach node of diff val or None
        while dupe_state:
            head = head.next
            if not head or head.val != tail.val:
                break
        
        # assign pointers after dupe state
        if not dupe_state:
            prev_node = prev_node.next
        else:
            prev_node.next = head
            dupe_state = False
        tail = head
        if head:
            head = head.next
    return dummy.next

l = llh.build_linked_list([1])
node = solution(l)
llh.print_linked_list(node)

