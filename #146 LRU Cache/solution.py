class LRUCache:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.val = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.dummy_head = self.Node(-1,-1)
        self.dummy_tail = self.Node(-1,-1)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else: # update existing node to head of list
            node = self.cache[key]
            self.makeNodeMostRecent(node)
            return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) == self.capacity: # replace oldest node with new node
                self.removeTail()
                self.addNode(key, value) # create node and add to head of linked list
            else: # length < capacity, simply add to head of list and add to cache
                self.addNode(key,value)
        else: # in cache, so update node's value and pointers
            node = self.cache[key]
            node.val = value
            self.makeNodeMostRecent(node) # update pointers

    # add new node to linkedList and cache
    def addNode(self,key:int, value:int)->None:
        node = self.Node(key,value)
        self.cache[key] = node
        node.next = self.dummy_head.next
        node.prev = self.dummy_head
        self.dummy_head.next = node
        if not self.dummy_tail.prev: # if adding first node
            self.dummy_tail.prev = node
        
    
    def removeTail(self)->None:
        tail = self.dummy_tail.prev
        tail.prev.next = tail.next
        tail.next.prev = tail.prev # update dummy_tail
        del self.cache[tail.key]

    def makeNodeMostRecent(self,node:Node)->None:
        # detach node 
        node.prev.next = node.next
        node.next.prev = node.prev
        
        node.next = self.dummy_head.next
        node.prev = self.dummy_head
        if not self.dummy_tail.prev: # if adding first node
            self.dummy_tail.prev = node



def main():
    obj = LRUCache(3)
    param_1 = obj.put(1,2)