from typing import List

import queue
from dataclasses import dataclass

@dataclass
class Node:
    node_id: int
    parents: List[int]
    children: List[int]
    num_unprocessed_parents: int

    def __lt__(self, other: "Node"):
        return self.num_unprocessed_parents < other.num_unprocessed_parents


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        """
        Edge list to node adjacency (ancestor) map // O(E)
        Start with "roots"
        dfs(node):
            result = dfs(parent) for parent in parents

        node {
            node_id
            parents
            num_unprocessed_parents
        }

        priority queue, maps nodes to number of unprocessed parents
        hashmap points to nodes in priority queue

        possible to dequeue a node with unprocessed parents?
        implies that there exists a parent which is unprocessed who has unprocessed parents
        said another way, if a graph is acyclic, there must exist a room which has no parents
        DAGS always have a node which has no parent
        Removing nodes from a DAG still leaves a DAG

        N + N-1 + N-2 + N-3....
        (N + 1)N/2

        create a hashmap that maps node_ids to Nodes    // O(N)
        for each edge, update that node's parents       // O(E)

        for each node, insert into the priority queue   // O(N)
        while queue is not empty, dequeue               // O(NlogN)
        for each dequeue, set the result to the
        concatenation of the results of the parents     // O(N * N)
        """
        nodes = {
            node_id: Node(node_id=node_id, parents=[], children=[], num_unprocessed_parents=0)
            for node_id in range(n)
        }

        for _from, to in edges:
            nodes[_from].children.append(nodes[to])
            nodes[to].parents.append(nodes[_from])
            nodes[to].num_unprocessed_parents += 1

        pq = queue.PriorityQueue()
        for node in nodes.values():
            pq.put(node)

        results = [None for _ in range(n)]
        while not pq.empty():
            node = pq.get()
            assert node.num_unprocessed_parents == 0
            
            results[node.node_id] = set()
            for parent in node.parents:
                results[node.node_id].add(parent.node_id)
                for parent_result in results[parent.node_id]:
                    results[node.node_id].add(parent_result)

            for child in node.children:
                child.num_unprocessed_parents -= 1

        results = [
            list(sorted(list(result)))
            for result in results
        ]
        print(results)
        return results


if __name__ == "__main__":
    Solution().getAncestors(2, [[0, 1]])
