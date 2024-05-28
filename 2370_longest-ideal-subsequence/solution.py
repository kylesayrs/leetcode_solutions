class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        """
        acfgbd
           |

        O(n^2)
        """
        cache = [0 for _ in range(len(s))]
        for index in reversed(range(len(s))):
            cache[index] = max(
                (
                    cache[next_index]
                    for next_index in range(index + 1, len(s))
                    if abs(ord(s[next_index]) - ord(s[index])) <= k
                ),
                default=0
            ) + 1

        return max(cache, default=0)
