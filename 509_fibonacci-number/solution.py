class Solution:
    def fib(self, n: int) -> int:
        if n <= 0:
            return 0

        if n < 3:
            return 1
        
        # set up memo
        prev_prev = 1
        prev = 1
        for _ in range(n - 2):
            # calculate
            f_n = prev_prev + prev

            # update memo
            prev_prev = prev
            prev = f_n

        return prev


if __name__ == "__main__":
    assert Solution().fib(1) == 1
    assert Solution().fib(2) == 1
    assert Solution().fib(3) == 2
    assert Solution().fib(4) == 3
    assert Solution().fib(5) == 5
