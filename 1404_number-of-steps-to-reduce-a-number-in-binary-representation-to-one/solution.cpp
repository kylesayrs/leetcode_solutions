#include <iostream>
#include <string>

/*
# right to left
# add carry if necessary
# if 0, +1 step
# if 1, add one, +2 steps
# save in carry
*/

class Solution {
public:
    int numSteps(std::string s) {
        // skip leading zeros
        int start = 0;
        while (start < s.size() && s[start] == '0') {
            start++;
        }

        // right to left simulation
        int total_steps = 0;
        int carry = 0;
        for (int i = s.size() - 1; i > start; i--) {
            int value = static_cast<int>(s[i] - '0') + carry;

            switch (value) {
                case 0:
                    total_steps += 1;
                    break;

                case 1:
                    total_steps += 2;
                    carry = 1;
                    break;

                case 2:
                    total_steps += 1;
                    carry = 1;
                    break;

                default:
                    assert(false);
            }
        }

        // end with 1, deal with carry
        if (carry == 1) {
            total_steps += 1;
        }

        return total_steps;
    }
};


int main() {
    Solution solution;
    solution.numSteps("1101");
}
