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




def solution(list1: ListNode, list2: ListNode) -> ListNode:
    head = ListNode()
    tail = head
    # if either has values
    while list1 or list2:
        if list2 and list1: # if neither nodes are null
            if list1.val <= list2.val:
                tail.next = list1
                tail = tail.next
                list1 = list1.next
            else:
                tail.next = list2
                tail = tail.next
                list2 = list2.next

        else: # if one node from a list is null
            if list2:
                tail.next = list2
                tail = tail.next
                list2 = list2.next
            else:
                tail.next = list1
                tail = tail.next
                list1 = list1.next
    return head.next


list1 = build_linked_list([])
list2 = build_linked_list([])
node = solution(list1, list2)
while node:
    print(node.val)
    node = node.next
print(node)