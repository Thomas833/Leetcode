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


def solution(head: ListNode, left: int, right: int)->ListNode:
    original = head
    stack = []
    counter = 1
    tail = None
    while head:
        if counter < left: # while counter less than left
            tail = head # capture last node before reversing
            head = head.next
            counter += 1
        else: # counter == left
            while counter <= right: # put nodes that need to be reversed in the stack
                stack.append(head)
                head = head.next
                counter += 1
            while stack: # pop nodes from stack and append them to tail
                if not tail:
                    tail = stack.pop()
                    original = tail
                    continue
                tail.next = stack.pop()
                tail = tail.next
            tail.next = head # set reversed node to rest of unreversed list
            break
    return original




ll = build_linked_list([1,3,5,7,9])
left = 2
right = 5
node = solution(ll, left, right)
while node:
    print(node.val)
    node = node.next