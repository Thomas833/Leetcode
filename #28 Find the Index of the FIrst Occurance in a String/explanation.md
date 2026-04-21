haystack = sadbutsad, needle =sad 

walk through the string in a while loop.
    - have two pointers that when used to create a substring from haystack, can be compared to needle
    - increment each pointer as you walk through string until first pointer reaches end of haystack
    - return -1 if reach end of string and last comparison not equal substring
    - if needle.length() > haystack.length(), return -1
    - return index if comparison of substring of haystack and needle is true

performance is O(n) because we will potentially walk through the entire string if its not there

completed and done on first try.