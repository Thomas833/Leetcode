# #83 Remove Duplicates from Sorted List - Explanation

O(n) time + space solution:
use set to determine if number in linked list already. if not, add it and increment, otherwise, remove node. 

O(n) time + O(1) space solution:

dummy.next = head
tail = dummy
dupe_state = False

if tail == dummy, increment both head and tail
move head ahead of tail. if head val equal tail, increment head and keep tail still (dupe_sate = True). when values differ or head is None, set tail.next = head and then set tail = head and set dupe_state = False. continue incrementing head until end of list
return dummy.next

                 h
dummy -> 1 -> 2
                 t