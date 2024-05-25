from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_dict = set(wordDict)

        cache: List[List[List[int]]] = [[] for _ in range(len(s))]
        cache.append([[]])  # last index base case

        for i in reversed(range(len(s))):
            for j in range(i, len(cache)):
                if s[i: j] in word_dict:
                    for word_break in cache[j]:
                        cache[i].append([wordDict.index(s[i: j])] + word_break)

        return [
            " ".join([wordDict[word_index] for word_index in word_break])
            for word_break in cache[0]
            if len(word_break) > 0
        ]


if __name__ == "__main__":
    Solution().wordBreak("catsanddog", ["cat","cats","and","sand","dog"])
    assert Solution().wordBreak("", ["cat","cats","and","sand","dog"]) == []
