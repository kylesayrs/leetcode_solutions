#include <iostream>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};


class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        TreeNode *current = root;
        while (true) {
            if (p->val < current->val && q->val < current->val) {
                current = current->left;
            
            } else if (p->val > current->val && q->val > current->val) {
                current = current->right;
            
            // case of split or either p or q is equal to root
            } else {
                return current;    
            }
        }
    }
};
