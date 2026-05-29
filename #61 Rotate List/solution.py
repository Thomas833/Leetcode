class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def build_linked_list(values: list[int]) -> ListNode | None:
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next

    return head
def print_linked_list(head):
    current = head

    while current:
        print(current.val, end=" -> ")
        current = current.next

    print("None")


def solution(head: ListNode, k: int)->ListNode:
    if not head or k == 0:
        return head
    
    dummy = ListNode(0,head)
    tail = dummy
    counter = 1

    # walk to end of list to get accurate length of list
    while head.next:
        head = head.next
        counter += 1
    
    # with accurate list length, reduce k to within length of list if k greater than list length
    k = k % counter
    if k == 0:
        return dummy.next
    
    # reset variables
    counter = 1
    head = dummy.next

    # move forward k nodes ahead of tail, which is at head of list. once counter > k, increment tail too
    while head.next:
        head = head.next
        counter += 1
        if counter > k:
            tail = tail.next
    
    # pointers are in place
    head.next = dummy.next # end node points to head of list, creating loop
    dummy.next = tail.next # set head of list to node after tail (tail is on node at end of list)
    tail.next = None # break loop and set new end of list to None

    return dummy.next
    

l = build_linked_list([1,2,3,4,5])
k = 1
print_linked_list(solution(l, k))
