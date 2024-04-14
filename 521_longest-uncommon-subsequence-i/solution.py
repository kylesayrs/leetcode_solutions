class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        # case len mismatch

        # case character mismatch
            # assert len(a) == len(b)
            # return len(a)

        # case order mismatch
            # can use any of the strings, since including it will guarantee not match

        if a == b:
            return -1

        return max(len(a), len(b))
