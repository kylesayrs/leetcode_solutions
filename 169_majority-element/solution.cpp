#include <vector>

class Solution {
public:
    int majorityElement(std::vector<int>& nums) {
        //assert(nums.size() <= 0)

        int majority_count = 0;
        int majority_value = nums[0];

        for (int index = 0; index < nums.size(); index++) {
            if (nums[index] == majority_value) {
                majority_count += 1;

            } else {
                majority_count -= 1;
            }

            if (majority_count < 0) {
                majority_count = 1;
                majority_value = nums[index];
            }
        }

        return majority_value;
    }
};
