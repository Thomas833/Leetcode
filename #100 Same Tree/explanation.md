# #100 Same Tree - Explanation

brute force would be walk through both trees in the same way and append each node's value to a list and compare the lists

first, check if both nodes are none, if so, return true.
if one is none, return false, 

since neither node is None, check the values, if they dont match, return false

recurse left and right and perform an "and" operation between them and return that to ensure each tree matches