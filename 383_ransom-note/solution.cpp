#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        cout << "canConstruct" << endl;
        int ransom_note_frequency[26];
        fill_n(ransom_note_frequency, 26, 0);

        for (char c : ransomNote) {
            ransom_note_frequency[c - 'a'] += 1;
        }

        for (char c : magazine) {
            ransom_note_frequency[c - 'a'] -= 1;
        }

        for (int freq : ransom_note_frequency) {
            if (freq > 0) {
                return false;
            }
        }

        return true;
    }
};


int main() {
    Solution solution;
    cout << solution.canConstruct("asdf", "fdas") << endl;
    cout << solution.canConstruct("asdf", "fdaszasdfasdf") << endl;
    cout << solution.canConstruct("asdfj", "fdaszasdfasdf") << endl;

    return 0;
}
