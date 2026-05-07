# #242 Valid Anagram - Explanation

- use a hashmap to track the characters found and the count for each one. use another hashmap to store the original count of s.
- iterate through t and check if the letter is in smap and, if so, check the count in tmap and ensure its less than that in smap. increment count. if not in smap, return False. 
- after filling out tmap, if i have not already returned False, i will iterate through tmap and compare each key and its respective count to those in smap. if they do not match, i.e. a count is less than necessary, return False. Else return True. 
- time complexity is O(n) and space complexity is O(n)
