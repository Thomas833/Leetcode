# #219 Contains Duplicates II - Explanation

inefficient method:
use nested loops to check if two indices match and abs(i-j) <= k

less efficient method:

- iterate through the list
    - check if element in hashmap. 
        - if yes, add index to list at key
        - if no, add value as key and add index to list
- iterate through hashmap
    - sort each list and see if the difference between first two elements is <=k
    return true if so, return false if get through entire hashmap




#0,1,2,3,4,5,6,7,8,9
[1,2,9,9], k=2, hashset = {2:1,9:2}
   |   |
more efficient method:
- iterate through list
    - have i = j = 0
    - if i == j, j+=1 and add hashset[nums[j]] = j
    - if abs(i-j) < k, check if nums[j] in hashset and if so, return true. if not, add it and j++
    - if abs(i-j) == k, check if nums[j] in hashset and if so, return true, otherwise pop nums[i] from hashset and i++ and j++

time complexity is O(n) and space complexity is O(n) because you could have n unique numbers where each one would go into the hashmap and you iterate through nums 1 time, so its linear
