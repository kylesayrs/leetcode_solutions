# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return version >= 5


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n + 1

        while left < right:
            # bias left, since we want to move left exclusively
            middle = (right - left) // 2 + left

            if isBadVersion(middle):
                right = middle

            else:
                left = middle + 1  # avoid infinite loop

        #assert left == right
        return left


if __name__ == "__main__":
    assert Solution().firstBadVersion(11) == 5
