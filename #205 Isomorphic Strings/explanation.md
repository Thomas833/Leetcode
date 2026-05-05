# #205 Isomorphic Strings - Explanation


use a hashmap to store the characters from one string as keys and map each one to a single character in the other string to determine if they are isomorphic

if s[i] not in hashmap, s[i] into hashmap key and t[i] as its value. 

if s[i] in hashmap, compare hashmap[s[i]] to t[i] and see if they match. if they match, continue. if not, return false. return true if reach end of loop.

need second hashmap to count string t to check if character from there is mapped to s that s doesnt know about easily since t[i] are values and cannot be looked up easily
example: s="pap", t="tte". 'a' is not in hashmap and we never check if t is already mapped with one hashmap

this solution is helpful. if not same length, cannot be isomorphic since order must be same
https://leetcode.com/problems/isomorphic-strings/solutions/4960160/beats-100-easiest-code-with-comments-exp-oxmr/?envType=study-plan-v2&envId=top-interview-150
