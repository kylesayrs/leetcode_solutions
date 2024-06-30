from typing import List


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        parents = [[] for index in range(n)]
        for _from, to in edges:
            parents[to].append(_from)

        topological_sort = []
        seen = set()
        def parentless(index: int):
            nonlocal topological_sort
            nonlocal seen

            if index in seen:
                return True
            
            for parent in parents[index]:
                if parentless(parent) == False:
                    seen.add(index)
                    return False

            topological_sort.append(index)
            seen.add(index)
            return True
        
        for node_index in range(n):
            parentless(node_index)

        results = [[] for _ in range(n)]
        for node_index in topological_sort:
            parent_ancestors = sum([
                results[parent]
                for parent in parents[node_index]
            ], start=[])
            results[node_index] = list(sorted(list(set(parents[node_index] + parent_ancestors))))

        return results


if __name__ == "__main__":
    Solution().getAncestors(5, [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]])
