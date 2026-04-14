import random
class RandomizedSet:

    def __init__(self):
       self.dictionary = {}
       self.values = [] 

    def insert(self, val: int) -> bool:
        if val not in self.dictionary:
            self.dictionary[val] = len(self.values)
            self.values.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
       if val not in self.dictionary:
            return False
       else:
            if len(self.values) > 1:
                idx = self.dictionary[val]
                self.values[idx] = self.values[-1]
                self.dictionary[self.values[-1]] = idx
                self.values[-1] = val
            self.values.pop()
            del self.dictionary[val]
            return True


    def getRandom(self) -> int:
        idx = random.randint(0,len(self.values)-1)
        return self.values[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()