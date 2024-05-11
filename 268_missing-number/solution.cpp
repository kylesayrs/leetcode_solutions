#include <iostream>
#include <vector>

using namespace std;

template <typename T>
void printVector(const std::vector<T>& vec) {
    std::cout << "[";
    for (size_t i = 0; i < vec.size(); ++i) {
        std::cout << vec[i];
        if (i != vec.size() - 1) {
            std::cout << ", ";
        }
    }
    std::cout << "]" << std::endl;
}

class Solution {
public:
    static int missingNumber(vector<int>& nums) {
        int missing_index = nums.size();
        for (int index = 0; index < nums.size(); index += 1) {
            while (nums[index] != index) {
                if (nums[index] >= nums.size()) {
                    missing_index = index;
                    break;
                }
                swap(nums[index], nums[nums[index]]);
            }
        }

        return missing_index;
    }
};


int main() {
    vector<int> nums = {2, 0};
    cout << Solution::missingNumber(nums) << endl;
}
