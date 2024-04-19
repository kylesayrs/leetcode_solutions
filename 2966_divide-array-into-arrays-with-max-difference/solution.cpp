#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> divideArray(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());

        vector<vector<int>> subarrays;
        for (unsigned i = 0; i < nums.size(); i += 3) {
            if (i + 2 >= nums.size()) {
                vector<vector<int>> empty_subarrays;
                return empty_subarrays;
            }

            vector<int> subarray {nums[i], nums[i + 1], nums[i + 2]};
            int subarray_max = *max_element(subarray.begin(), subarray.end());
            int subarray_min = *min_element(subarray.begin(), subarray.end());

            if ((subarray_max - subarray_min) > k) {
                vector<vector<int>> empty_subarrays;
                return empty_subarrays;
            }

            subarrays.push_back(subarray);
        }

        return subarrays;
    }
};
