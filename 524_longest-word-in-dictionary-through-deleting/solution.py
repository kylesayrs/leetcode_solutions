from typing import List


class Solution:
    def is_subsequence(subsequence: str, string: str) -> bool:
        string_index = 0
        subseq_index = 0

        while string_index < len(string):
            if subsequence[subseq_index] == string[string_index]:
                subseq_index += 1

                if subseq_index >= len(subsequence):
                    return True
            
            string_index += 1
        
        return False
    

    def getLongest(a: str, b: str) -> str:
        if len(a) > len(b):
            return a
        
        if len(b) > len(a):
            return b
        
        return a if a < b else b
            

    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        ret_word = ""

        for subsequence in dictionary:
            if Solution.is_subsequence(subsequence, s):
                ret_word = Solution.getLongest(ret_word, subsequence)

        return ret_word
