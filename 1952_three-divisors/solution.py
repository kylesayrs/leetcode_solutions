import math


class Solution:
    def isThree(self, n: int) -> bool:
        n_sqrt = math.sqrt(n)
        div_upper_bound = (
            int(math.ceil(n_sqrt))
            if int(n_sqrt) != n_sqrt
            else int(n_sqrt) + 1
        )

        for div in range(2, div_upper_bound):
            if n % div == 0:
                if div * div == n:
                    return True
                else:
                    return False

        return False
