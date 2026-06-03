# #146 LRU Cache - Explanation

counter to track length of linked list
have hashmap store key as key, and node as value with value given inside


capacity = 2
cache = {2:2,1:1}

put(1,1)
put(2,2)
get(1)

              
head <-> 2 -> 1 <-> tail

if counter less than capacity, add it to head of doubly linked list and map and increase counter

get(key)
check if key in cache. 
if yes, return node's value and update node to head of list
if no, return -1

put(key, value)
if in cache:
        update node's value, adjust neighbor's pointers, and bring node to head of list
else:
    if length(cache) < capacity:
        add node to head of list and add node to cache
    else: length == capacity and key,value not in cache
        remove node previous to tail (oldest node), update its neighbor's pointers, remove from cache, and create new node and add it to head of list and add it to map
