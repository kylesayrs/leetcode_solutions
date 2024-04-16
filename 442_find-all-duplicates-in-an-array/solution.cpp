#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        // yes I understand this is O(n) space but I don't think doing index
        // jumbling is particularly enlightening
        vector<int> duplicates;
        for (size_t i = 0; i < nums.size(); i++) {
            size_t index = abs(nums[i]) - 1;

            // if seen a negative, this means our other pair marked as negative
            // therefore we're a duplicate
            if (nums[index] < 0) {
                duplicates.push_back(index + 1);
            }

            // mark with negative
            nums[index] = -nums[index];
        }
        
        return duplicates;
    }
};


int main(int argc, char **argv) {
    Solution solution;
    vector<int> nums = {4, 2, 3, 4, 1}; // uses the constructor
    vector<int> duplicates = solution.findDuplicates(nums);

    for (int duplicate : duplicates) {
        cout << duplicate << endl;
    }
}
