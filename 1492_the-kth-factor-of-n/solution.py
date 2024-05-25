import math


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        left_factors = []
        right_factors = []

        for factor_candidate in range(1, math.floor(math.sqrt(n) + 1)):
            if n % factor_candidate == 0:
                factor_pair = n // factor_candidate

                left_factors.append(factor_candidate)
                right_factors.append(n // factor_candidate)

                if factor_candidate == factor_pair:
                    right_factors.pop()

            if len(left_factors) >= k:
                return left_factors[len(left_factors) - k - 1]

        distance_from_right_end = len(right_factors) - 1 - (k - len(left_factors) - 1)
        if distance_from_right_end < 0:
            return -1

        return right_factors[distance_from_right_end]


if __name__ == "__main__":
    assert Solution().kthFactor(7, 2) == 7
    assert Solution().kthFactor(4, 4) == -1
    assert Solution().kthFactor(12, 3) == 3
    assert Solution().kthFactor(1, 1) == 1
    assert Solution().kthFactor(24, 6) == 8
