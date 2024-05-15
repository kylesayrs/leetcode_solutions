#include <iostream>
#include <string>

using namespace std;


class Solution {
public:
    string addBinary(string a, string b) {
        int a_index = 0;
        int b_index = 0;

        cout << a[0] << endl;
        cout << b[0] << endl;


        string sum_string;
        while (true) {
            int a_digit = (a_index < a.size()) ? a[a_index] - '0' : 0;
            int b_digit = (b_index < b.size()) ? b[b_index] - '0' : 0;
            cout << a_digit << ", " << b_digit << endl;

            if (a_digit == 0 && b_digit == 0) {
                break;
            }

            sum_string = to_string(a_digit + b_digit) + sum_string;

            a_index++;
            b_index++;
        }

        cout << sum_string << endl;
        return sum_string;
    }
};


int main() {
    Solution().addBinary("1", "0");
}
