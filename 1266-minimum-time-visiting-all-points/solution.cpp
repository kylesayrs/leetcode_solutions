#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
    int minTimeToVisitAllPoints(vector<vector<int>>& points) {
        int time_elapsed = 0;
        int points_size = points.size();
        for (int index = 0; index < points_size - 1; index++) {
            // I really hate this overly optimized code
            // I'd rather be storing values in variables which
            // explain their significance, but apparently
            // the leetcode compiler isn't smart enough to
            // optimize the memory & runtime if I write that way
            time_elapsed += max(
                abs(points[index + 1][0] - points[index][0]),
                abs(points[index + 1][1] - points[index][1])
            );
        }

        return time_elapsed;
    }
};


int main(int argc, char** argv) {
    Solution solution;

    vector<vector<int>> points({{1, 1}, {3, 4}, {-1, 0}});
    //vector<vector<int>> points({{3, 4}, {-1, 0}});


    cout << solution.minTimeToVisitAllPoints(points) << endl;
}
