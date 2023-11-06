#include <iostream>

using namespace std;


struct ListNode {
    int val;
    ListNode *next;
};


void printListNode(ListNode *list_node) {
    cout << "ListNode(";
    ListNode *current_node = list_node;
    while (current_node != NULL) {
        if (current_node != list_node) {
            cout << ", ";
        }
        cout << current_node->val;
        current_node = current_node->next;
    }

    cout << ")" << endl;
}


ListNode *makeNumber(std::initializer_list<int> number_list) {
    assert (number_list.begin() != number_list.end());
    ListNode *head = NULL;
    ListNode *parent = head;

    for (const int *digit = number_list.begin(); digit != number_list.end(); digit++) {
        if (parent == NULL) {
            head = new ListNode({*digit, NULL});
            parent = head;
        } else {
            parent->next = new ListNode({*digit, NULL});
            parent = parent->next;
        }
    }

    return head;
}


class Solution {
    public:
        ListNode *addTwoNumbers(ListNode *list_one, ListNode *list_two) {
            // initialize nodes
            ListNode *node_one = list_one;
            ListNode *node_two = list_two;
            int carry = 0;

            // initialize solution
            ListNode *solution_head = NULL;
            ListNode *solution_parent = solution_head;

            // while still have things to add
            while (node_one != NULL or node_two != NULL or carry != 0) {
                int node_one_val = node_one != NULL ? node_one->val : 0;
                int node_two_val = node_two != NULL ? node_two->val : 0;

                // perform addition
                int sum = node_one_val + node_two_val + carry;
                int digit = sum % 10;
                carry = sum >= 10 ? 1 : 0;

                // store solution
                if (solution_parent == NULL) {
                    solution_parent = new ListNode({digit, NULL});
                    solution_head = solution_parent;
                } else {
                    solution_parent->next = new ListNode({digit, NULL});
                    solution_parent = solution_parent->next;
                }

                // iterate list nodes
                if (node_one != NULL) {
                    node_one = node_one->next;
                }
                if (node_two != NULL) {
                    node_two = node_two->next;
                }
            }

            // special case of zero
            if (solution_head == NULL) {
                solution_head = new ListNode({0, NULL});
            }

            return solution_head;
        }
};


int main(int argc, char **argv) {
    Solution solution;

    ListNode *num_one = makeNumber({0, 1, 2});
    printListNode(num_one);

    ListNode *num_two = makeNumber({0});
    printListNode(num_two);

    ListNode *sum = solution.addTwoNumbers(num_one, num_two);
    printListNode(sum);
    return 0;
}
