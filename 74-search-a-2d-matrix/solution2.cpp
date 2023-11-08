#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        // assert(matrix.size() > 0)
        int matrix_height = matrix.size();
        int matrix_width = matrix[0].size();

        int left_row = 0;
        int left_col = 0;

        // right is one beyond last element position
        int right_row = matrix_height - 1;
        int right_col = matrix_width;

        while (true) {
            int left_global = left_row * matrix_width + left_col;
            int right_global = right_row * matrix_width + right_col;
            int index_global = ((right_global - left_global) >> 1) + left_global;
            int index_row = index_global / matrix_width;
            int index_col = index_global % matrix_width;

            int index_value = matrix[index_row][index_col];

            if (target < index_value) {
                if (index_row == right_row && index_col == right_col) {
                    return false;
                }

                right_row = index_row;
                right_col = index_col;
                continue;
            }

            if (target > index_value) {
                if (index_row == left_row && index_col == left_col) {
                    return false;
                }

                left_row = index_row;
                left_col = index_col;
                continue;
            }

            // target == index_value
            //cout << index_row << ", " << index_col << endl;
            return true;
        }
    }
};


int main(int argc, char **argv) {
    Solution solution;

    vector<vector<int>> matrix({{1, 2, 3}, {4, 5, 6}, {7, 8, 9}});
    int target = 5;

    bool in_matrix = solution.searchMatrix(matrix, target);
    cout << in_matrix << endl;
}
