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



def OnSolution(head: ListNode, k: int)->ListNode:
    stack = []
    original = None
    counter = 1
    linkNode = None
    populatedNode = None # first node in each k group
    while head:
        # append nodes to stack to reverse
        while counter <= k and head:
                if not populatedNode:
                    populatedNode = head
                stack.append(head)
                head = head.next
                counter += 1
            
        # stack is filled with nodes to reverse. now reverse their pointers
        if counter > k or head:
            while stack:
                if not linkNode:
                    original = stack[-1]
                    linkNode = stack.pop()
                    continue
                linkNode.next = stack.pop()
                linkNode = linkNode.next
            # reset variable for next group
            counter = 1
            populatedNode = None
            if not head: # if head points to None, at end of list and set last linkNode to Null
                linkNode.next = None
        else:
            linkNode.next = populatedNode
    return original


def effecientSolutionRecursive(head: ListNode, k: int)->ListNode:
    if not head:
        return head
        
    curr = head
    prev = None
    k_remain = k
    while curr and k_remain > 0:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        k_remain -= 1

    if k_remain == 0:
        # we have reached end of the k-block reversal, 
        # prev points to the begin of the reversed block
        # head points to the end of the reversed block
        head.next = effecientSolutionRecursive(curr, k)
        return prev
    else:
        # we have reached end of the list with less then k node in the block
        # reverse back and return the head
        curr = prev
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return head


def efficientSolutionIterative(head: ListNode, k: int)->ListNode:
    dummy = ListNode(0, head)
    group_prev = dummy

    def get_kth_node(start: ListNode, k: int):
        while start and k > 0:
            start = start.next
            k -= 1
        
        return start

    while True:
        # Find the k-th node from group_prev
        kth_node = get_kth_node(group_prev, k)
        if not kth_node:
            break
        group_next = kth_node.next

        # Reverse the group
        prev, cur = kth_node.next, group_prev.next
        while cur != group_next:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        # Reconnect the reversed group with the rest of the list
        temp = group_prev.next
        group_prev.next = kth_node
        group_prev = temp

    return dummy.next


ll = build_linked_list([1,2,3,4,5])
k = 2
#node = OnSolution(ll, k)
node = efficientSolutionIterative(ll,k)
while node:
    print(node.val)
    node = node.next