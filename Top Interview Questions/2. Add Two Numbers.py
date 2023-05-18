# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = result = ListNode()

        while l1 or l2 or carry != 0:

            if l1:
                num1 = l1.val
            else:
                num1 =  0
            
            if l2:
                num2 = l2.val
            else:
                num2 = 0


            sum = num1 + num2 + carry

            if sum >= 10:
                carry = 1
            else:
                carry = 0

            if l1 != None:
                l1 = l1.next
            
            if l2 != None:
                l2 = l2.next
            



            result.next = ListNode(sum%10)
            result = result.next
        
        return head.next
