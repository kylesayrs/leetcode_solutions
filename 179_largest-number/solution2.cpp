#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    static bool cmp(string a, string b) {
        string a_first = a + b;
        string b_first = b + a;
        return a_first > b_first;
    }

    string largestNumber(vector<int>& nums) {
        // convert to strings
        vector<string> nums_strings;
        nums_strings.reserve(nums.size());
        for (int num : nums) {
            nums_strings.push_back(to_string(num));
        }

        // sort using custom sort
        sort(nums_strings.begin(), nums_strings.end(), &Solution::cmp);

        // generate string
        string result;
        for (string num_string : nums_strings) {
            result += num_string;
        }

        // edge case, leading zeros means all zeros
        if (result.size() > 0 && result[0] == '0') {
            return "0";
        }

        return result;
    }
};

int main() {
    Solution solution;
    vector<int> input = {0, 0};
    string result = solution.largestNumber(input);

    cout << result << endl;
}
