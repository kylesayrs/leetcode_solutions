"""
Modify to support duplicate values

We could keep a frequency map, then use the key + frequency to index
A better way would be to keep a stack in the index_lookup
    Since the stack always maintains least to greatest index order, we know
    We can swap the last indices when swapping from the back
"""
from typing import Dict, List

import random
from collections import defaultdict


class RandomizedSet:
    def __init__(self):
        self.index_lookup: Dict[int, List[int]] = defaultdict(lambda: [])
        self.array: List[int] = []


    def insert(self, value: int) -> bool:
        value_present = len(self.index_lookup[value]) > 0

        self.index_lookup[value].append(len(self.array))
        self.array.append(value)

        return not value_present


    def remove(self, value: int) -> bool:
        if len(self.index_lookup[value]) <= 0:
            return False

        index = self.index_lookup[value][-1]
        last_index = len(self.array) - 1
        last_value = self.array[last_index]

        self.index_lookup[value].remove(index)
        if last_value != value:
            self.index_lookup[last_value].remove(last_index)
            self.index_lookup[last_value].append(index)
        self.array[index], self.array[last_index] = self.array[last_index], self.array[index]
        self.array.pop()

        return True


    def getRandom(self) -> int:
        return random.choice(self.array)
