#include <iostream>
#include <string>

class Solution {
public:
    std::string addBinary(std::string a, std::string b) {
        // TODO: check for edge cases
        int a_index = a.size() - 1;
        int b_index = b.size() - 1;
        unsigned carry = 0;

        std::string sum_string;
        while (a_index >= 0 || b_index >= 0 || carry >= 1) {
            unsigned a_part = a_index >= 0 ? static_cast<unsigned>(a[a_index]) - static_cast<unsigned>('0') : 0;
            unsigned b_part = b_index >= 0 ? static_cast<unsigned>(b[b_index]) - static_cast<unsigned>('0') : 0;

            unsigned part_sum = a_part + b_part + carry;
            if (part_sum >= 2) {
                part_sum -= 2;
                carry = 1;
            } else {
                carry = 0;
            }
    
            sum_string = static_cast<char>(part_sum + '0') + sum_string;

            a_index--;
            b_index--;
        }

        return sum_string;
    }
};


int main() {
    Solution solution;
    assert(solution.addBinary("01011", "1011") == "10110");
}
