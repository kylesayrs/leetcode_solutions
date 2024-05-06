#include <stdio.h>

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode *slow_ptr = head;
        ListNode *fast_ptr = head;

        while (slow_ptr && fast_ptr && fast_ptr->next) {
            slow_ptr = slow_ptr->next;
            fast_ptr = fast_ptr->next->next;

            // impossible for slow_ptr to be NULL
            if (slow_ptr == fast_ptr) {
                return true;
            }
        }

        return false;


    }
};
