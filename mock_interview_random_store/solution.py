from typing import Dict, List

import random


class Store:
    def __init__(self):
        self.index_lookup: Dict[int, int] = {}
        self.array: List[int] = []


    def insert(self, value: int):
        self.index_lookup[value] = len(self.array)
        self.array.append(value)


    def remove(self, value: int):
        index = self.index_lookup[value]
        last_index = len(self.array) - 1
        self.array[index], self.array[last_index] = self.array[last_index], self.array[index]

        del self.index_lookup[value]
        self.array.pop()


    def get_random(self) -> int:
        return random.choice(self.array)
