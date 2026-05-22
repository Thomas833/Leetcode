# #2 Add Two Numbers - Explanation
first method that comes to mind

set heads of each list to nodes
walk through each list and perform math to get the numbers combined. 
reverse numbers
perform addition
create linked list, walking through each digit

O(n+m+k) time complexity and O(k)


=================

perform single digit addition with carry and output to new linked list as you calculate each digit
482 + 65

482
 65+
___


2->8->4
5->6
^
carry = 1
output = 7->4->5
