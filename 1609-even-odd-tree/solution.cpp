#include <iostream>
#include <vector>

using namespace std;


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
};


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
#define FAST_MOD2(num) (num & 1)


class Solution {
public:
    bool isEvenOddHelper(TreeNode* node, int level, vector<int> &prev_by_level) {
        if (node == nullptr) {
            return true;
        }

        int node_value = node->val;
        bool node_is_odd = FAST_MOD2(node_value);
        bool level_is_odd = FAST_MOD2(level);

        // check number value parity rule
        if (level_is_odd == node_is_odd) {
            return false;
        }
        
        // check if first node in level
        if (level >= prev_by_level.size()) {
            prev_by_level.push_back(node_value);

        // check ascending/descending rule
        } else {
            int prev_level_value = prev_by_level[level];

            if (node_value == prev_level_value) {
                return false;
            }

            if (level_is_odd) {
                if (node_value > prev_level_value) {
                    return false;
                }
            } else {
                if (node_value < prev_level_value) {
                    return false;
                }
            }

            prev_by_level[level] = node_value;
        }

        // recurse on children
        return (
            isEvenOddHelper(node->left, level + 1, prev_by_level) &&
            isEvenOddHelper(node->right, level + 1, prev_by_level)
        );
    }


    bool isEvenOddTree(TreeNode* root) {
        vector<int> level_buffer;

        return isEvenOddHelper(root, 0, level_buffer);
    }
};


int main(int argc, char **argv) {
    Solution solution;

    TreeNode root({1});

    TreeNode n1({10});
    TreeNode n2({4});
    root.left = &n1;
    root.right = &n2;

    TreeNode n3({3});
    n1.left = &n3;
    n1.right = nullptr;

    TreeNode n4({7});
    TreeNode n5({9});
    n2.left = &n4;
    n2.right = &n5;

    cout << solution.isEvenOddTree(&root) << endl;

    return 0;
}
