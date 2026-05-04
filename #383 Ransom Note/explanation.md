# #383 Ransom Note - Explanation

To solve this problem, we want to use a hashmap. In the hashmap, we will store the lowercase english letter as the key, and the count that we have for that character that we can use in the ransom note. We will walk through the magazine string once to populate the hashmap. We will then walk through the ransom note string and query the hashmap if the character is a key, and if so, is the value greater than 0. If we do have a valid character and count greater than 0, decrement the count by 1. Continue until return false or end loop and return true. 

Time complexity is O(m+r) (linear) and space complexity is O(m). 

NUANCE: because the hashmap will at MAX ever only hold 26 characters, the space complexity is effectively O(1) due to the very small max size that it can be. 