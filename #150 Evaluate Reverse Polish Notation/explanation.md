# #150 Evaluate Reverse Polish Notation - Explanation

we must use a stack to perform the computations. for each number, push them to the stack. if we come across an operand, remove the top two numbers, perform the computation, and return that number to the top of the stack. continue until there is nothing left in the stack
