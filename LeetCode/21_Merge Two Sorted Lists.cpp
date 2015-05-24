/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* head = NULL;
        ListNode* tail = NULL;
        ListNode* ptr1 = l1;
        ListNode* ptr2 = l2;
        if (!l1 && !l2) {
            return NULL;
        } else if (!l1) {
            return l2;
        } else if (!l2) {
            return l1;
        } else if (l1->val < l2->val) {
            head = l1;
            ptr1 = ptr1->next;
        } else {
            head = l2;
            ptr2 = ptr2->next;
        }
        tail = head;

        
        
        return head;
    }
};