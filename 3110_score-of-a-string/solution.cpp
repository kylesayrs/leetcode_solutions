#include <string>


class Solution {
public:
    int scoreOfString(std::string s) {
        std::string offset = s.substr(1);

        // normally we'd check for a size of one

        int sum = 0;
        for (int i = 0; i < offset.size(); i++) {
            sum += std::abs(s[i] - offset[i]);
        }

        return sum;
    }
};
