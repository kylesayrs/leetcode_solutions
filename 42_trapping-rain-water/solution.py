from typing import List, Tuple


class Solution:
    def helper(left: int, height: List[int]) -> Tuple[int, int]:
        total_water = 0
        for right in range(left, len(height)):
            if height[right] >= height[left]:
                # total area between posts
                section_width = max(right - left - 1, 0)
                section_height = min(height[left], height[right])
                section_water = section_width * section_height
                # print(f"section: {left} {right}")
                # print(f"section_water: {section_water}")
                
                # subtract integral
                for index in range(left + 1, right):  # TODO check
                    section_water -= height[index]
                    # print(f"subtracing... {index}: {height[index]}")

                # add to total
                total_water += section_water

                # update left
                left = right

        return total_water, left
    

    def trap(self, height: List[int]) -> int:
        total_water_left_middle, left = Solution.helper(0, height)
        # print((total_water_left_middle, left))

        total_water_in_right_section, left = Solution.helper(0, list(reversed(height[left:])))
        # print((total_water_in_right_section, left))

        return total_water_left_middle + total_water_in_right_section

        


if __name__ == "__main__":
    assert Solution().trap([10, 5, 10, 5, 8, 1, 2]) == (5 + 3 + 1)
    assert Solution().trap([4, 2, 0, 3, 2, 5]) == 9

    assert Solution().trap([100, 1, 1, 1, 1, 2]) == 4
    assert Solution().trap([100, 1, 1, 1, 1, 1]) == 0
    assert Solution().trap([100, 1, 1, 1, 1, 0]) == 0
    assert Solution().trap([100, 1, 1, 1, 1, 120]) == (400 - 4)

    assert Solution().trap([100, 3, 2, 3, 2, 1, 2]) == 2
    assert Solution().trap([0, 2, 1, 2, 3, 2, 3]) == 2
