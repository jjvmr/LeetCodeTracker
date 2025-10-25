# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Helper function to convert linked list → integer
        def listnode_to_int(node):
            num_str = ""
            while node:
                num_str = str(node.val) + num_str  # prepend because digits are reversed
                node = node.next
            return int(num_str)

        # Helper function to convert integer → linked list
        def int_to_listnode(num):
            dummy = ListNode(0)
            curr = dummy
            for d in str(num)[::-1]:
                curr.next = ListNode(int(d))
                curr = curr.next
            return dummy.next

         # Convert both linked lists to integers
        n1 = listnode_to_int(l1)
        n2 = listnode_to_int(l2)

        # Perform addition
        total = n1 + n2

        # Convert back to linked list
        return int_to_listnode(total)

        # l1num = int(''.join(map(str, l1[::-1])))
        # l2num = int(''.join(map(str, l2[::-1])))
        
        # calc = l1num + l2num
        # rev_calc = list(map(int, str(calc)))
        # return rev_calc[::-1]

        