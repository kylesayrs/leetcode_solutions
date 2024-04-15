#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int getSequentialNumber(int first_digit, int num_digits) {
        int sequential_number = 0;
        int digit = first_digit;
        for (int i = num_digits; i > 0; i--) {
            sequential_number += digit * pow(10, i - 1);
            digit++;
        }

        return sequential_number;
    }

    vector<int> sequentialDigits(int low, int high) {
        vector<int> sequential_digits;

        unsigned num_low_digits = log10(low) + 1;
        unsigned num_high_digits = log10(high) + 1;

        for (unsigned num_digits = num_low_digits; num_digits <= num_high_digits; num_digits++) {
            for (unsigned first_digit = 1; first_digit <= 9; first_digit++) {
                if (num_digits > 10 - first_digit) {
                    continue;
                }

                int sequential_number = getSequentialNumber(first_digit, num_digits);

                if (sequential_number < low || sequential_number > high) {
                    continue;
                }

                sequential_digits.push_back(sequential_number);
            }
        }

        return sequential_digits;

        // for each digit position between low and high

            // for each digit in that position
                // if place is not in range, continue
                // construct sequential starting at that position
                // if the number is lower than low, skip
    }
};


int main(int argc, char **argv) {
    Solution solution;

    // int sequential_number = solution.getSequentialNumber(1, 3);
    // cout << sequential_number << endl;
    // sequential_number = solution.getSequentialNumber(1, 8);
    // cout << sequential_number << endl;
    // sequential_number = solution.getSequentialNumber(6, 3);
    // cout << sequential_number << endl;

    //vector<int> sequential_digits = solution.sequentialDigits(1000, 13000);
    vector<int> sequential_digits = solution.sequentialDigits(123456789, 1000000000);

    for (int digits : sequential_digits) {
        cout << digits << endl;
    }
}
