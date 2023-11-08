#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
    int binaryLeftSearch(vector<int> &nums, int target, bool &found) {
        int left = 0;
        int right = nums.size();
        found = false;

        while (true) {
            int index = ((right - left) >> 1) + left;
            int index_value = nums[index];

            //cout << left << index << right << endl;

            if (target < index_value) {
                if (index == right) {
                    return -1;
                }

                right = index;
                continue;
            }

            if (target > index_value) {
                if (index == left) {
                    return index;  // return the left bound on the target
                }

                left = index;
                continue;
            }

            // target == index_value
            found = true;
            return index;
        }
    }


    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        vector<int> first_column;
        for (int i = 0; i < matrix.size(); i++) {
            first_column.push_back(matrix[i][0]);
        }

        bool found;
        int left_row_index = binaryLeftSearch(first_column, target, found);
        if (found) {
            cout << left_row_index << ", " << 0 << endl;
            return true;
        }
        if (left_row_index < 0) {
            return false;
        }

        int left_column_index = binaryLeftSearch(matrix[left_row_index], target, found);
        cout << left_row_index << ", " << left_column_index << endl;
        return found;
    }
};


int main(int argc, char **argv) {
    Solution solution;

    vector<vector<int>> matrix({{1, 2, 3}, {2, 6, 7}, {5, 7, 8}});
    int target = 3;

    bool in_matrix = solution.searchMatrix(matrix, target);
    cout << in_matrix << endl;
}
