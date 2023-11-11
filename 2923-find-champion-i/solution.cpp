#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
    int findChampion(vector<vector<int>> &grid) {
        int grid_size = grid.size();

        for (int i = 0; i < grid_size; i++) {
            for (int j = 0; j < grid_size; j++) {
                if (i == j) {
                    continue;
                }
                if (grid[i][j] == 0) {
                    goto not_champion;
                }
            }
            return i;

            not_champion:
            continue;
        }

        // champion not found
        return -1;
    }
};


int main(int argc, char **argv) {
    Solution solution;

    vector<vector<int>> grid({{0, 1}, {0, 0}});

    int champion_index = solution.findChampion(grid);
    cout << champion_index << endl;
}
