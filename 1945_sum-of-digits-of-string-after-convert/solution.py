class Solution:
    def getLucky(self, s: str, k: int) -> int:
        a = ord('a')
        s = "".join(str(ord(c) - a + 1) for c in s)
        for _ in range(k):
            _sum = sum((int(c) for c in s), start=0)
            s = str(_sum)
        return _sum
        
