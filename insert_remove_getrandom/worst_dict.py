import random

class RandomizedSet:

    def __init__(self):
        self.l = {}

    def insert(self, val: int) -> bool:
        if val in self.l:
            return False
        else:
            self.l[val] = None
            return True

    def remove(self, val: int) -> bool:
        if val in self.l:
            del self.l[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(list(self.l.keys()))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()