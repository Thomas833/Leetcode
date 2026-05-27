class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(values: list[int]) -> Node | None:
    if not values:
        return None

    head = Node(values[0])
    current = head

    for value in values[1:]:
        current.next = Node(value)
        current = current.next

    return head

def solution(head: Node)-> Node:
    #if head is empty
    if not head:
        return None
    
    #need to initialize with None pair to cover when you lookup None
    hashmap = {None:None}
    cur = head

    # populate hashmap with old node as key and newly created node as value.
    while cur:
        hashmap[cur] = Node(cur.val)
        cur = cur.next

    # iterate through original linked list again. populate next and random pointers with hashmap lookups
    cur = head
    while cur:
        copy = hashmap[cur]
        copy.next = hashmap[cur.next]
        copy.random = hashmap[cur.random]
        cur = cur.next
    #return head of new list
    return hashmap[head]
