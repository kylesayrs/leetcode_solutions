#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
    int findChampion(int n, vector<vector<int>>& edges) {
        vector<bool> is_champion_candidate(n, true);

        int edges_size = edges.size();
        for (int edge_index = 0; edge_index < edges_size; edge_index++) {
            int weaker_team_index = edges[edge_index][1];
            is_champion_candidate[weaker_team_index] = false;
        }

        int champion_index = -1;
        for (int team_index = 0; team_index < n; team_index++) {
            if (is_champion_candidate[team_index]) {
                if (champion_index != -1) { 
                    return -1;
                }

                champion_index = team_index;
            }
        }

        return champion_index;
    }
};


int main(int argc, char **argv) {
    Solution solution;

    /*
    int num_teams = 3;
    vector<vector<int>> edges({
        {0, 1},
        {1, 2}
    });
    */

    int num_teams = 5;
    vector<vector<int>> edges({
        {0, 2},
        {1, 3},
        {1, 2},
        {1, 0}
    });

    int champion = solution.findChampion(num_teams, edges);
    cout << champion << endl;
}
