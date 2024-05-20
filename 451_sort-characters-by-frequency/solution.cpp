#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>


class Solution {
public:
    std::string frequencySort(std::string s) {
        std::unordered_map<char, size_t> char_to_freq;
        for (char &c : s) {
            if (char_to_freq.find(c) == char_to_freq.end()) {
                char_to_freq[c] = 1;
            } else {
                char_to_freq[c] += 1;
            }
        }

        std::vector<char> freq_to_char[s.size() + 1];
        for (std::pair<char, size_t> key_value : char_to_freq) {
            freq_to_char[key_value.second].push_back(key_value.first);
        }

        std::string output;
        for (int freq = s.size(); freq >= 0; freq--) {
            for (char c : freq_to_char[freq]) {
                for (int i = 0; i < freq; i++) {
                    output += c;
                }
            }
        }

        return output;
    }
};


int main() {
    Solution solution;
    std::string input;
    std::cin >> input;
    solution.frequencySort(input);
}
