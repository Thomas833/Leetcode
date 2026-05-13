# #57 Insert Interval - Explanation

if we wanted a less efficient solution, we could insert the new interval into the array, sort, and then walk through the array and merge any overlapping intervals. This gives O(n) complexity and is an earlier leetcode problem (#56 Merge Intervals)

a more efficient method is to do one pass and do the merging since the array is already sorted. this should give O(n) time complexity and O(1) space complexity

ask chatgpt for help explaining this one as the solutions are convoluted



