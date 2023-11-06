#include <iostream>
#include <vector>

using namespace std;


template <typename T>
void printVector(vector<T> vector) {
    cout << "vector(";
    for (int i = 0; i < vector.size(); i++) {
        if (i != 0) {
            cout << ", ";
        }
        cout << vector[i];
    }
    cout << ")" << endl;
}


class Solution {
    public:
        vector<int> twoSum(vector<int>& nums, int target) {
            std::unordered_map<int, int> value_lookup;

            for (int i = 0; i < nums.size(); i++) {
                int addend = target - nums[i];

                if (value_lookup.find(addend) != value_lookup.end()) {
                    vector<int> indicies{i, value_lookup[addend]}; 
                    return indicies;
                }

                value_lookup.insert({nums[i], i});
            }

            vector<int> no_solution{-1, -1}; 
            return no_solution;
        }
};


int main(int argc, char **argv) {
    Solution solution;

    vector<int> nums {0, 4, 3, 0};
    int target = 0;
    vector<int> indices = solution.twoSum(nums, target);
    printVector(indices);
    return 0;
}
