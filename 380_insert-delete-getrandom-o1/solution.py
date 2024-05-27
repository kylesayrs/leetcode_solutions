from typing import Dict, List

import random


class RandomizedSet:
    def __init__(self):
        self.index_lookup: Dict[int, int] = {}
        self.array: List[int] = []


    def insert(self, value: int) -> bool:
        if value in self.index_lookup:
            return False
        
        self.index_lookup[value] = len(self.array)
        self.array.append(value)

        return True


    def remove(self, value: int) -> bool:
        if value not in self.index_lookup:
            return False
        
        index = self.index_lookup[value]
        last_index = len(self.array) - 1
        last_value = self.array[last_index]

        self.index_lookup[last_value] = index
        self.array[index], self.array[last_index] = self.array[last_index], self.array[index]
        
        del self.index_lookup[value]
        self.array.pop()

        return True


    def getRandom(self) -> int:
        return random.choice(self.array)


if __name__ == "__main__":
    random_set = RandomizedSet()
    assert random_set.insert(0) == True
    assert random_set.getRandom() == 0
    # print(random_set.index_lookup)
    # print(random_set.array)
    assert random_set.insert(0) == False
    # print(random_set.index_lookup)
    # print(random_set.array)
    assert random_set.remove(0) == True
    # print(random_set.index_lookup)
    # print(random_set.array)
    assert random_set.insert(0) == True
