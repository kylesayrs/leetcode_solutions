class Solution:
    def shortest_distance_in_ring(i: int, j: int, size: int):
        return min((i - j) % size, (j - i) % size)


    def findRotateSteps(self, ring: str, key: str) -> int:

        cache = {}
        def dfs(ring_index: int, key_index: int):
            nonlocal ring
            nonlocal key
            nonlocal cache

            if (ring_index, key_index) in cache:
                return cache[(ring_index, key_index)]
            
            if key_index == len(key):
                cache[(ring_index, key_index)] = 0
            
            else:    
                cache[(ring_index, key_index)] = min(
                    dfs(next_index, key_index + 1) + Solution.shortest_distance_in_ring(next_index, ring_index, len(ring)) + 1
                    for next_index in range(len(ring))
                    if ring[next_index] == key[key_index]
                )

            return cache[(ring_index, key_index)]

        return dfs(0, 0)


if __name__ == "__main__":
    Solution().findRotateSteps("godding", "gd")
    Solution().findRotateSteps("godding", "godding")
    Solution().findRotateSteps("a", "a")
    Solution().findRotateSteps("abcde", "ade")
