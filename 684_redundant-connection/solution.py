from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        node_ids = set(
            [edge[0] for edge in edges] +
            [edge[1] for edge in edges]
        )

        parents = {node_id: node_id for node_id in node_ids}
        ranks = {node_id: 1 for node_id in node_ids}

        def find_parent(node_id: int) -> int:
            if parents[node_id] != node_id:
                parents[node_id] = find_parent(parents[node_id])  # path compression
            return parents[node_id]

        def union(node1: int, node2: int) -> bool:
            parent1 = find_parent(node1)
            parent2 = find_parent(node2)

            if parent1 == parent2:
                return False

            if ranks[parent1] > ranks[parent2]:
                parents[parent2] = parent1
                ranks[parent2] += ranks[parent1]
            else:
                parents[parent1] = parent2
                ranks[parent1] += ranks[parent2]

            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
