# #155 Min Stack - Explanation

the tricky part of this problem is keeping track of the minimum at all times, even when you could possibly pop the current minimum. 

the solution is at each index in the stack, store both the value and the minimum at that time. This way, no matter what value is at the top, we know what the minimum is. 
