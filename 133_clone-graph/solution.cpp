#include <vector>
#include <unordered_map>

using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};

class Solution {
public:
    static Node* dfsClone(Node* node, unordered_map<Node*, Node*> &cloned_nodes) {
        if (!node) {
            return NULL;
        }

        if (cloned_nodes.find(node) == cloned_nodes.end()) {
            cloned_nodes[node] = new Node(node->val);
            for (unsigned i = 0; i < node->neighbors.size(); i++) {
                cloned_nodes[node]->neighbors.push_back(
                    Solution::dfsClone(node->neighbors[i], cloned_nodes)
                );
            }
        }

        return cloned_nodes[node];
    }

    static Node* cloneGraph(Node* node) {
        unordered_map<Node*, Node*> cloned_nodes;
        return dfsClone(node, cloned_nodes);
    }
};


int main(int argc, char **argv) {
    Node *node = new Node(1);

    Node *cloned_node = Solution::cloneGraph(node);

    delete node;
}
