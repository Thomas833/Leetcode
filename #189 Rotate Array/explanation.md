The key here is to use a reverse function to reverse the entire array or subsections of the array.
Also, since k can be larger than the length of the array, we need to use modulus to tell us how many times we need to actually rotate it. 
    If k = 2 and lenth = 7, 2 % 7 = 2 since 7 goes into 2 0 times with remainder 2. 
    But if k = 10 and length = 7, 10 % 7 = 3 since 7 goes into 10 1 time with remainder 3.

The algorithm is pretty simple. Reverse the entire array, then reverse the [0,k-1] section of numbers, which are the numbers that should be rotated, and then rotate the rest of the array.

Original array: [1,2,3,4,5,6,7], k = 3
Reverse entire array: [7,6,5,4,3,2,1]
Reverse [0,k-1]: [5,6,7,4,3,2,1]
Reverse [k, len(nums) - 1]: [5,6,7,1,2,3,4]


This accomplishes the goal in O(n) time complexity and O(1) space comlexity


