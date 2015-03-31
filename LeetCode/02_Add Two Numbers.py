# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        point = l1
        val = 0
        power = 0
        while point:
            val += point.val * 10 ** power
            power += 1
            point = point.next

        point = l2
        power = 0
        while point:
            val += point.val * 10 ** power
            power += 1
            point = point.next

        pre = None
        val = str(val)
        for x in val:
            ans = ListNode(x)
            ans.next = pre
            pre = ans
        return ans