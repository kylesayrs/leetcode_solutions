#include <iostream>

using namespace std;


class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int start = 0;
        int end = 0;

        int longest_length = 0;

        for (int end = 0; end < s.length(); end++) {
            for (int index = start; index < end; index++) {
                if (s[index] == s[end]) {
                    start = index + 1;  // one after the offending position
                    break;
                }
            }

            int substring_length = end - start + 1;
            if (substring_length > longest_length) {
                longest_length = substring_length;
            }
        }

        return longest_length;
    }
};

int main(int argc, char **argv) {
    Solution solution;

    int length = solution.lengthOfLongestSubstring("pwwkew");
    cout << length << endl;
}
