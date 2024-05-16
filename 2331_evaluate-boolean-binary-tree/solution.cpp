#include <stdexcept>

using namespace std;


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};



class Solution {
public:
    bool evaluateTree(TreeNode* root) {
        /*
        if (!root) {
            throw invalid_argument("invalid node");
        }
        */

        switch (root->val) {
            case 0:
                return false;

            case 1:
                return true;

            case 2: {
                bool left_val = evaluateTree(root->left);
                bool right_val = evaluateTree(root->right);
                return left_val || right_val;
            }

            case 3: {
                bool left_val = evaluateTree(root->left);
                bool right_val = evaluateTree(root->right);
                return left_val && right_val;
            }

            default:
                throw invalid_argument("invalid node");
        }
    }
};
