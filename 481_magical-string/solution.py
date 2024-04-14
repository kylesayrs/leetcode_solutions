from collections import deque


class Solution:
    def magicalString(self, n: int) -> int:
        num = 1
        occurences = deque([1])

        total_ones = 1

        s = []
        for _ in range(n):
            s.append(str(num))
            if num == 1:
                total_ones += 1


            occurences[0] -= 1
            if occurences[0] <= 0:
                occurences.popleft()
                num = 2 - num + 1

            occurences.append(num)

        return total_ones
    

    def magicalString(self, n: int) -> int:
        num = 1
        occurence_index = 0
        total_ones = 0

        occurences = []
        for _ in range(n):
            occurences.append(num)
            if num == 1:
                total_ones += 1

            occurences[occurence_index] -= 1
            if occurences[occurence_index] <= 0:
                occurence_index += 1
                num = 2 - num + 1

        return total_ones


    def magicalString(self, n: int) -> int:
        num = 1
        occurences = deque()
        total_ones = 0

        for _ in range(n):
            occurences.append(num)
            if num == 1:
                total_ones += 1

            occurences[0] -= 1
            if occurences[0] <= 0:
                occurences.popleft()
                num = 2 - num + 1

        return total_ones
    

if __name__ == "__main__":
    assert Solution().magicalString(6) == 3
    assert Solution().magicalString(1) == 1
    assert Solution().magicalString(19) == 9
