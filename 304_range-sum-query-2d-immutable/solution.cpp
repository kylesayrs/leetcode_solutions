#include <iostream>
#include <vector>

using namespace std;

class NumMatrix {
public:
    NumMatrix(vector<vector<int>>& matrix) {
        int height = matrix.size();
        //assert(height > 0);
        int width = matrix[0].size();

        prefix_sum_matrix.reserve(height);
        for (int i = 0; i < height; i++) {
            vector<int> row_vector;
            row_vector.reserve(width);
            int row_prefix_sum = 0;

            for (int j = 0; j < width; j++) {
                int prev_row_prefix_sum = (i - 1 >= 0) ? prefix_sum_matrix[i - 1][j] : 0;
                row_prefix_sum += matrix[i][j];
                row_vector.push_back(row_prefix_sum + prev_row_prefix_sum);
            }

            prefix_sum_matrix.push_back(row_vector);
        }
    }

    int sumRegion(int row1, int col1, int row2, int col2) {
        int left_sum = (col1 - 1 >= 0) ? prefix_sum_matrix[row2][col1 - 1] : 0;
        int top_sum = (row1 - 1 >= 0) ? prefix_sum_matrix[row1 - 1][col2] : 0;
        int left_top_sum = (row1 - 1 >= 0 && col1 - 1 >= 0) ? prefix_sum_matrix[row1 - 1][col1 - 1] : 0;

        return prefix_sum_matrix[row2][col2] - left_sum - top_sum + left_top_sum;
    }

    vector<vector<int>> prefix_sum_matrix;
};


void printMatrix(const std::vector<std::vector<int>>& matrix) {
    for (const auto& row : matrix) {
        for (int num : row) {
            std::cout << num << "\t";
        }
        std::cout << std::endl;
    }
}


/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */


int main() {
    vector<vector<int>> matrix_input;
    matrix_input.push_back({1, 2, 3});
    matrix_input.push_back({1, 2, 3});
    matrix_input.push_back({1, 2, 3});
    NumMatrix matrix(matrix_input);

    printMatrix(matrix.prefix_sum_matrix);
}
