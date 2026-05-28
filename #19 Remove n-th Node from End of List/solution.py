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


def solution(head: ListNode, n: int)-> ListNode:
    dummy = ListNode(0,head)
    forward = head
    prev_node = dummy
    counter = 1

    # increment forward along list
    while counter < n:
        forward = forward.next
        counter += 1
    
    # iterate through list until forward reaches end node
    while forward.next:
        forward = forward.next
        prev_node = prev_node.next
        head = head.next

    # set rewrite previous node to removal node's .next
    prev_node.next = head.next
    return dummy.next


l = build_linked_list([1])
n = 1
node = solution(l, n)
while node:
    print(node.val)
    node = node.next
