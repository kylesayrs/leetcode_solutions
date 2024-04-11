from typing import List, Set


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        node_dependents = {}
        num_nodes = 0

        # ingest data into child dictionary
        for dependent, dependency in prerequisites:
            if dependent not in node_dependents:
                node_dependents[dependent] = []

            if dependency not in node_dependents:
                node_dependents[dependency] = []

            node_dependents[dependency].append(dependent)

        # if there are more unique courses than allowed, we can't take them all
        if len(node_dependents) > numCourses:
            return False

        # check if node or any of its dependents have cycles
        cycleless = set()
        def has_cycle(node: int, seen: Set[int]):
            # already checked by previous call
            if node in cycleless:
                return False

            # already seen in this recursion call
            if node in seen:
                return True
            
            # check dependents
            seen.add(node)
            _has_cycle = any(
                has_cycle(dependent, seen)
                for dependent in node_dependents[node]
            )
            seen.remove(node)  # remember to move seen to avoid branch collision

            # cache result globally
            if not _has_cycle:
                cycleless.add(node)
            
            return _has_cycle

        # check each node for cycles
        for node in node_dependents:
            seen = set()
            if has_cycle(node, seen):
                return False
                    
        return True


if __name__ == "__main__":
    assert Solution().canFinish(10, [[2, 0], [1, 0], [0, 1], [1, 2], [8, 9]]) == False
    assert Solution().canFinish(10, [[1, 0]]) == True
    assert Solution().canFinish(10, [[1, 0], [0, 1]]) == False
    assert Solution().canFinish(10, [[1, 0], [2, 1], [0, 2]]) == False
    assert Solution().canFinish(10, [[1, 0], [2, 1], [0, 2], [5, 6]]) == False
    assert Solution().canFinish(10, [[1, 0], [2, 1], [0, 2], [1, 0]]) == False
    assert Solution().canFinish(10, [[1, 0], [2, 1], [0, 3], [1, 0]]) == True

        
