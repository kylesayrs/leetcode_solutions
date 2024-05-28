#include <string>

class Solution {
public:
    int equalSubstring(std::string s, std::string t, int maxCost) {
        int n = s.size();

        int letter_costs[n];
        for (int i = 0; i < n; i++) {
            letter_costs[i] = std::abs(static_cast<int>(s[i]) - static_cast<int>(t[i]));
        }

        int left = 0;
        int max_substring_len = 0;
        int substring_cost = 0;
        for (int right = 1; right < n + 1; right++) {
            substring_cost += letter_costs[right - 1];
            while (substring_cost > maxCost) {
                substring_cost -= letter_costs[left];
                left += 1;
            }

            max_substring_len = std::max(max_substring_len, right - left);
        }

        return max_substring_len;
    }
};
