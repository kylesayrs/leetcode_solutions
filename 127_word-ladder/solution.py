from typing import List, Dict

from collections import defaultdict, deque


class Solution:
    blank_char: str = "_"

    def get_word_masks(word: str) -> List[str]:
        return [
            f"{word[:char_index]}{Solution.blank_char}{word[char_index + 1:]}"
            for char_index in range(len(word))
        ]


    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # ingest edge list
        edge_list: Dict[str, List[str]] = defaultdict(lambda: [])
        for word in wordList + [beginWord]:
            word_masks = Solution.get_word_masks(word)
            for word_mask in word_masks:
                edge_list[word_mask].append(word)

        # store word distances
        word_distances = {
            word: 0
            for word in wordList
        }

        #print(edge_list)

        # bfs from endWord
        queue = deque()
        seen = set()
        queue.append((endWord, 0))
        while len(queue) > 0:
            # pop from queue
            word, distance = queue.popleft()

            # success condition
            if word == beginWord:
                #print(word_distances)
                return distance + 1  # counting number of words in sequence
            
            # seen condition
            if word in seen:
                continue
            seen.add(word)

            # update distances
            word_distances[word] = distance

            # collect edges
            edges = set(sum([
                    edge_list[word_mask]
                    for word_mask in Solution.get_word_masks(word)
                ],
                []
            ))

            # recurse on edges
            for edge_word in edges:                
                queue.append((edge_word, distance + 1))

        return 0


if __name__ == "__main__":
    assert Solution().ladderLength("zabc", "abcd", ["abcd", "abcc", "abbc", "aabc"]) == 5
    assert Solution().ladderLength("a", "c", ["a", "b", "c"]) == 2
    assert Solution().ladderLength("a", "c", ["b", "c"]) == 2
    assert Solution().ladderLength("a", "c", ["c"]) == 2
    assert Solution().ladderLength("a", "c", ["a", "c"]) == 2

    assert Solution().ladderLength("a", "c", ["a", "b"]) == 0

    assert Solution().ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == 5
