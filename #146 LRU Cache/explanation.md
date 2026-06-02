# #146 LRU Cache - Explanation

counter to track length of linked list
have hashmap store key as key, and node as value with value given inside

length = 1
capacity = 3
hm = []


h                            t
dummy <-> 1 dummy

if counter less than capacity, add it to head of doubly linked list and map and increase counter


if in cache:
        update node's value and pointers
else:
    if length < capacity:
        add node to head of list and add node to map and increase length
    else:
        remove oldest node from list and cache and add node to head of list and add to cache
