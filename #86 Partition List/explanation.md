# #86 Partition List - Explanation


INITIALIZATIONS:
dummy is node pointing to head
tail set to dummy
newHead set to is None
stack for nodes less than x

x = 3               NH
                                       h
dummy -> 1X -> 2X -> 3 -> 4 -> 1X -> None
                          t

if head.val < x, put head node in stack. also, set tail.next to head.next. otherwise, increment head and tail

if newHead is None and head.val >= x, set newHead to head.

if head is None and newHead is None, return dummy.next since list is either empty or all values less than x

otherwise, if newHead has Node, then append all nodes in stack to newHead.
