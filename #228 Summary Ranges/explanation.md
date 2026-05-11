# #228 Summary Ranges - Explanation

[0,1,2,4,5,7]

iterate through the array once
    - have pointers that point to the left and right side of the range. the the number to the right of the pointer is not 1 above it, append a string with the numbers from the two pointers.set both pointers to the the next number. if it is 1 above, increase right range. 
