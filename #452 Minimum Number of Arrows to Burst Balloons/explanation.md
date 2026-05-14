# #452 Minimum Number of Arrows to Burst Balloons - Explanation

sort list
set prevInt to first element
count = 0
iterate through list starting at second interval
    # if curInt[0] is greater than prevInt[1], add 1 to count since no overlap. set prevInt to curInt

l   # if curInt[0] is less than or equal to prevInt[1], we have overlap.

O(nlogn) and O(1)


