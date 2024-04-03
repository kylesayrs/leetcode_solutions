import math


class Solution:
    def __init__(self):
        self.cache = {}


    def min_steps_helper(self, x: int, a: int, target: int) -> int:
        if x in self.cache and a in self.cache[x]:
            return self.cache[x][a]

        if x > target:
            return math.inf
        
        if x == target:
            return 0
        
        steps = min(
            2 + self.min_steps_helper(x + x, x, target), # copy and paste
            1 + self.min_steps_helper(x + a, a, target)  # paste
        )

        if x not in self.cache:
            self.cache[x] = {}

        self.cache[x][a] = steps

        return steps


    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        
        return 2 + self.min_steps_helper(2, 1, n)
                

if __name__ == "__main__":
    print(Solution().minSteps(1))
    print(Solution().minSteps(3))
    print(Solution().minSteps(1))
