for clarification:
s1 = "abc"
s2 = "bca"

These are permutations because:

both have a, b, c
just shuffled differently
- - - - - - - - 

Method:
    1. Check length of two strings. If same, walk through both strings in for loop and store count of each character in tuple and char as key. first index of tuple is for s1 and second is for s2. After first iteration, iterare through hashmap and compare tuple values. if each tuple pair doesn't match, then return False. Time complexity O(n) and space complexity O(n) due to hashmap