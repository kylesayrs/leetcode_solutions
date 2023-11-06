#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left_bound = 0;
        int right_bound = nums.size();

        while (true) {
            int index = ((right_bound - left_bound) >> 1) + left_bound;
            int index_value = nums[index];

            if (target < index_value) {
                if (right_bound == index) {
                    return -1;
                }

                // index is guaranteed to be less than right_bound
                right_bound = index;
                continue;
            }

            if (target > index_value) {
                if (left_bound == index) {
                    return -1;
                }

                // index is guaranteed to be greater than left_bound
                left_bound = index;
                continue;
            }

            // index_value == target
            return index;
        }
    }
};


int main(int argc, char **argv) {
    Solution solution;

    vector<int> nums({-1,0,3,5,9,12});
    int target = 9;

    int index = solution.search(nums, target);
    cout << index << endl;
}
