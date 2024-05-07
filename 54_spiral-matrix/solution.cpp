#include <iostream>
#include <vector>

using namespace std;


enum Direction { right, down, left, up };

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int height = matrix.size();
        int width = matrix[0].size();

        Direction direction = Direction::right;
        int direction_bounds[4] = {width, height, 0, 0};

        vector<int> result;
        int pos[2] = {0, 0};
        while (
            direction_bounds[Direction::left] < direction_bounds[Direction::right] &&
            direction_bounds[Direction::up] < direction_bounds[Direction::down]
        ) {
            // record result
            result.push_back(matrix[pos[0]][pos[1]]);
            //cout << pos[0] << "," << pos[1] << endl;
            //cout << direction_bounds[0] << direction_bounds[1] << direction_bounds[2] << direction_bounds[3] << endl;

            // switch directions and update bounds
            switch (direction) {
                case Direction::right:
                    if (pos[1] + 1 >= direction_bounds[direction]) {
                        direction_bounds[Direction::up] += 1;
                        direction = Direction::down;
                    }
                    break;

                case Direction::down:
                    if (pos[0] + 1 >= direction_bounds[direction]) {
                        direction_bounds[Direction::right] -= 1;
                        direction = Direction::left;
                    }
                    break;

                case Direction::left:
                    if (pos[1] - 1 < direction_bounds[direction]) {
                        direction_bounds[Direction::down] -= 1;
                        direction = Direction::up;
                    }
                    break;

                case Direction::up:
                    if (pos[0] - 1 < direction_bounds[direction]) {
                        direction_bounds[Direction::left] += 1;
                        direction = Direction::right;
                    }
                    break;
            }

            // move direction
            switch (direction) {
                case Direction::right:
                    pos[1] += 1;
                    break;

                case Direction::down:
                    pos[0] += 1;
                    break;

                case Direction::left:
                    pos[1] -= 1;
                    break;

                case Direction::up:
                    pos[0] -= 1;
                    break;
            }
        }
        
        return result;
    }
};


int main(int argc, char **argv) {
    Solution solution;

    vector<vector<int>> matrix;
    matrix.push_back({1, 2, 3});
    matrix.push_back({4, 5, 6});
    matrix.push_back({7, 8, 9});

    vector<int> result = solution.spiralOrder(matrix);
    
    cout << "result: " << endl;
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << endl;
    }

    return 0;
}
