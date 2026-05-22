from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def solution(head: Optional[ListNode]) -> bool:
    fast = head
    slow = head
    if head == None:
        return False

    while True:
        if fast != None:
            fast = fast.next
            if fast != None:
                fast = fast.next
            else:
                break
            slow = slow.next
        else:
            break
        if fast is slow:
            return True
    return False

# 2->1->3->4
#    ^-----|
head = ListNode(2)
node1 = ListNode(1)
head.next = node1
node2 = ListNode(3)
node1.next = node2
node3 = ListNode(4)
node2.next = node3
node3.next = node1

print(solution(head))
