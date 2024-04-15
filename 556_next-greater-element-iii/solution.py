class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = [int(char) for char in str(n)]

        if len(digits) <= 1:
            return -1

        first_swappable_index = len(digits) - 2
        while first_swappable_index >= 0:
            value = digits[first_swappable_index]
            prev_value = digits[first_swappable_index + 1]

            if value < prev_value:
                break

            first_swappable_index -= 1

        else:
            return -1

        swap_index = len(digits) - 1
        while digits[swap_index] <= digits[first_swappable_index]:
            swap_index -= 1

        tmp = digits[first_swappable_index]
        digits[first_swappable_index] = digits[swap_index]
        digits[swap_index] = tmp

        digits[first_swappable_index + 1:] = sorted(digits[first_swappable_index + 1:])

        result = int("".join([str(d) for d in digits]))
        if result >= 2**31:
            return -1
        
        return result



if __name__ == "__main__":
    assert Solution().nextGreaterElement(115) == 151
    assert Solution().nextGreaterElement(511) == -1
    assert Solution().nextGreaterElement(151) == 511
    assert Solution().nextGreaterElement(115) == 151
    assert Solution().nextGreaterElement(10) == -1
    assert Solution().nextGreaterElement(2147483486) == -1
