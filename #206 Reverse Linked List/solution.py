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

def iterative(head: ListNode)->ListNode:
    
    stack = [] # initialize stack
    
    # iterate through list, pushing values onto stack
    while head:
        stack.append(head.val)
        head = head.next

    # pop from stack and append value to new node. stop when stack empty
    dummy = ListNode()
    tail = dummy
    while stack:
        node = ListNode(stack.pop())
        tail.next = node
        tail = tail.next
    return dummy.next

def recursive(head: ListNode)->ListNode:
    if head.next == None:
        return head
    else:
        new_head = recursive(head.next)
        head.next.next = head
        head.next = None
        return new_head
    
ll = build_linked_list([0,1,3,4])
node = recursive(ll)
while node:
    print(node.val)
    node = node.next