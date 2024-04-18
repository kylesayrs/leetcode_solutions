from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        can_break = [False for _ in range(len(s))]
        can_break += [True]

        for i in reversed(range(len(s))):
            for word in wordDict:
                if (
                    s[i:].startswith(word) and
                    can_break[i + len(word)]
                ):
                    can_break[i] = True
                    break

        return can_break[0]
    

if __name__ == "__main__":
    assert Solution().wordBreak("asdf", ["df", "as"]) == True
    assert Solution().wordBreak("leetcode", ["leet", "code"]) == True
    assert Solution().wordBreak("applepenapple", ["apple", "pen"]) == True
    assert Solution().wordBreak("catsandog", ["cats","dog","sand","and","cat"]) == False
    assert Solution().wordBreak("catsandog", ["catasdfasdfasdfasdfasdfasdfasdfasdfasdfs","catsandog","sand","and","cat"]) == True
