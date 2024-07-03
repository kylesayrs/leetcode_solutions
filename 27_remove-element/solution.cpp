#include <vector>
#include <algorithm>

class Solution {
public:
    int removeElement(std::vector<int>& nums, int val) {
        size_t pointer = 0;
        for (size_t index = 0; index < nums.size(); index++) {
            if (nums[index] != val) {
                std::swap(nums[pointer], nums[index]);
                pointer++;
            }
        }

        return pointer;
    }
};
