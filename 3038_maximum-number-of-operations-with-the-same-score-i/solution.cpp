#include <vector>

class Solution {
public:
    int maxOperations(std::vector<int>& nums) {
        size_t n = nums.size();
        size_t index = 0;

        bool score_set = false;
        int score = 0;
        int num_operations = 0;
        while (index + 1 < n) {
            if (!score_set) {
                score = nums[index] + nums[index + 1];
                score_set = true;
                continue;
            }

            if (nums[index] + nums[index + 1] != score) {
                break;
            }

            num_operations++;
            index += 2;
        }

        return num_operations;
    }
};
