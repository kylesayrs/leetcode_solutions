#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    size_t getMiddleRadius(string &s, size_t middle) {
        size_t offset = 1;
        while (
            (static_cast<int>(middle - offset) >= 0) && (middle + offset <= s.length() - 1) &&
            (s[middle - offset] == s[middle + offset])
        )
            offset++;

        // step back one to get last valid offset
        return offset - 1;
    }

    size_t getLeftRadius(string &s, size_t left) {
        size_t right = left + 1;
        size_t offset = 1;
        while (
            (static_cast<int>(right - offset) >= 0) && (left + offset <= s.length() - 1) &&
            (s[right - offset] == s[left + offset])
        )
            offset++;

        // step back one to get last valid offset
        return offset - 1;
    }

    string longestPalindrome(string s) {
        string longest_palidrome = "";

        for (size_t i = 0; i < s.length(); i++) {
            // character is middle
            size_t middle_radius = getMiddleRadius(s, i);

            size_t middle_palidrome_length = 2 * middle_radius + 1;
            if (middle_palidrome_length > longest_palidrome.length()) {
                longest_palidrome = s.substr(i - middle_radius, middle_palidrome_length);
            }

            // character is left of middle
            size_t left_radius = getLeftRadius(s, i);

            size_t left_palidrome_length = 2 * left_radius;
            if (left_palidrome_length > longest_palidrome.length()) {
                longest_palidrome = s.substr(i - left_radius + 1, left_palidrome_length);
            }
        }

        return longest_palidrome;
    }
};


int main(int argc, char **argv) {
    Solution solution;
    string palidrome = solution.longestPalindrome("asdf");
    cout << palidrome << endl;

    palidrome = solution.longestPalindrome("babad");
    cout << palidrome << endl;

    palidrome = solution.longestPalindrome("cbbd");
    cout << palidrome << endl;

    return 0;
}
