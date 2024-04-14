class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        # case len mismatch
            # return longest, since you cannot form a subsequence from a string
            # which is shorter than the subsequence
        
        # otherwise, they have the same length

        # case character mismatch
            # return length, since you cannot form a subsequence from a string
            # if the subsequence has a character the string doesn't

        # case order mismatch
            # return length, since you cannot form a subsequence from a string
            # if the subsequence has a character the string doesn't
        
        # if the order matches and the character matches, they must be the same
        # in which case there is no uncommon subsequence

        if a == b:
            return -1

        return max(len(a), len(b))
