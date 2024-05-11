#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    static int concatenate(int a, int b) {
        int num_digits = (b == 0) ? 1 : static_cast<int>(log10(b)) + 1;
        int a_offset = static_cast<int>(pow(10, num_digits));

        return a * a_offset + b;
    }

    static bool cmp(int a, int b) {
        int a_first = Solution::concatenate(a, b);
        int b_first = Solution::concatenate(b, a);
        return a_first > b_first;
    }

    string largestNumber(vector<int>& nums) {
        // sort using custom sort
        sort(nums.begin(), nums.end(), &Solution::cmp);

        // generate string
        string result;
        for (int num : nums) {
            result += to_string(num);
        }

        return result;
    }
};

int main() {
    Solution solution;
    vector<int> input = {1, 2, 3, 32};
    string result = solution.largestNumber(input);

    cout << result << endl;
}
