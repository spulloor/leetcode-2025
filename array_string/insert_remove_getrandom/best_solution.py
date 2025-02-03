import random

class RandomizedSet:

    def __init__(self):
        self.l = []
        self.d = {}

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False


        self.d[val] = len(self.l)
        self.l.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val in self.l:
            '''
            last_element = self.l[-1]
            position = self.d[val]

            self.l[position] = last_element
            self.d[last_element] = position

            '''
            last_element, position = self.l[-1], self.d[val]

            self.l[position], self.d[last_element] = last_element, position


            self.l.pop()
            del self.d[val]

            return True


        return False

    def getRandom(self) -> int:
        return random.choice(self.l)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()