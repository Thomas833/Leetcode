# #57 Insert Interval - Explanation

if we wanted a less efficient solution, we could insert the new interval into the array, sort, and then walk through the array and merge any overlapping intervals. This gives O(n) complexity

a more efficient method is to do one pass and do the merging since the array is already sorted. this should give O(n) time complexity and O(1) space complexity

different scenarios

newInterval=[0,2], intervals=[[3,4]] 
newInterval=[0,3], intervals=[[2,4]]
newInterval=[3,4], intervals=[[2,4]]
newInterval=[6,7], intervals=[[2,4]]
newInterval=[4,6], intervals=[[2,4]]


intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
intervals = [[1,3],[6,9]], newInterval = [2,5]
intervals = [[2,5],[6,7],[8,9]], newInterval = [0,1]

