#include <iostream>
#include <vector>
#include <map>
#include <stdio.h>


class Solution {
public:
    static int maxSubarrayLength(std::vector<int>& nums, int k) {
        std::map<int, int> freq;        // maps `num`s to frequency in subarray 
        int max_subarray_len = 0;

        int left = 0;
        int nums_size = nums.size();
        for (int right = 0; right < nums_size; right++) {
            // unpack num
            int num = nums[right];
            freq[num] += 1;         // freq defaults to 0

            while (freq[num] > k) {
                freq[nums[left]] -= 1; 
                left += 1;
            }
            
            max_subarray_len = std::max(max_subarray_len, right - left + 1);
        }
        
        return max_subarray_len;
    }
};


int main(int argc, char **argv) {
    std::vector<int> nums = {1, 1, 1, 3};
    printf("%d\n", Solution::maxSubarrayLength(nums, 2));

    return 0;
}
