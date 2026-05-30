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


def solution(head: ListNode, x: int)-> ListNode:
    dummy = ListNode(0,head)
    newHead = None
    tail = dummy
    stack = []

    # walk through linked list
    while head:
        if head.val < x:
            tail.next = head.next
            stack.append(head)
        else:
            if not newHead:
                newHead = head
            tail = tail.next
        head = head.next
    
    # pop elements from stack, point them to newHead, and set newHead to new node
    while stack:
        node = stack.pop()
        node.next = newHead
        newHead = node

    return newHead

l = build_linked_list([])
x = 3
print_linked_list(solution(l,3))
