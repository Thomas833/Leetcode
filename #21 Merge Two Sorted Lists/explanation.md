# #21 Merge Two Sorted Lists - Explanation

first, determine which head of the list is smallest. if the pointer is None, continue to append the other list

if both have elements:

- choose which has smallest head. That will be the priority list
- create two additional pointers that will walk ahead of the original ones to determine which way to merge elements
- if element is smaller in non-priority list next node, set current node next pointer to non-priority node, increment non-priority pointer to next node, and set non-priority pointer to point to next priority node. 


list1 = [],           list2 = []
list1 = [1,2,4],      list2 = []
list1 = [],           list2 = [1,4,6,7]
list1 = [-5,1,5],     list2 = [1,2,3]
list1 = [-10,3,5],    list2 = [0,2,3]
list1 = [0,3,5],      list2 = [-3,9,30]


                 tail
head = 0 -> -5 -> -1
        
list2 = [-5, 0, 2],     
            l2
        
list1 = [-1, 1, 3]
            l1