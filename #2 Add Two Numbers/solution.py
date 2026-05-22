class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solution(l1: ListNode, l2: ListNode):
    tail = ListNode(0)
    it = tail
    carry = 0
    while l1 or l2:
        if l1 and l2:
            total = l1.val + l2.val + carry
            if total >= 10:
                node = ListNode(total-10)
                carry = 1
            else:
                node = ListNode(total)
                carry = 0  
            l1 = l1.next
            l2 = l2.next
        elif l1 and not l2:
            total = l1.val + carry
            if total >= 10:
                node = ListNode(total - 10)
                carry = 1
            else:
                node = ListNode(total)
                carry = 0
            l1 = l1.next
        elif not l1 and l2:
            total = l2.val + carry
            if total >= 10:
                node = ListNode(total - 10)
                carry = 1
            else:
                node = ListNode(total)
                carry = 0
            l2 = l2.next
        tail.next = node
        tail = tail.next
    if carry:
        tail.next = ListNode(carry)
    return it.next
        





def build_linked_list(arr):
    dummy = ListNode(0)
    tail = dummy

    for val in arr:
        tail.next = ListNode(val)
        tail = tail.next

    return dummy.next

l1 = build_linked_list([9,9,9,9,9,9,9])
l2 = build_linked_list([9,9,9,9])

node = solution(l1,l2)

while node != None:
    print(node.val)
    node = node.next







# here is simplified version of what we have:
def addTwoNumbers(self, l1: ListNode, l2: ListNode) ->ListNode:

        dummy = ListNode(0)

        current = dummy

        carry = 0


        while l1 or l2 or carry:

            val1 = l1.val if l1 else 0

            val2 = l2.val if l2 else 0


            total = val1 + val2 + carry


            carry = total // 10

            digit = total % 10


            current.next = ListNode(digit)

            current = current.next


            if l1:

                l1 = l1.next


            if l2:

                l2 = l2.next


        return dummy.next
