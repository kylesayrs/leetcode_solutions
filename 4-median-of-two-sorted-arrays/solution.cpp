#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        
        return 0.0;
    }
};

int main(int argc, char **argv) {
    Solution solution;

    vector<int> nums1({1, 2, 3});
    vector<int> nums2({1, 2, 3});

    int median = solution.findMedianSortedArrays(nums1, nums2);
    cout << median << endl;
}
