/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode* ptr = NULL;
    struct ListNode* index = head;
    struct ListNode* temp;
    while (index) {
        temp = index->next;
        index->next = ptr;
        ptr = index;
        index = temp;
    }
    return ptr;
}