from typing import List

import math


class Solution:
    def countBits(self, n: int) -> List[int]:
        bit_counts = [0]

        for i in range(1, n + 1):
            most_sig_bit_mask = 1 << math.floor(math.log2(i))
            bit_counts.append(bit_counts[i - most_sig_bit_mask] + 1)

            #print(f"{i:010b}, {most_sig_bit_mask:010b}, {(i - most_sig_bit_mask):010b}, {bit_counts[i]}")

        return bit_counts


if __name__ == "__main__":
    Solution().countBits(7)
