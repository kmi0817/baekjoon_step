# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        linked_list = []
        
        if not head :
            return True
        
        node = head
        while node is not None :
            linked_list.append(node.val)
            node = node.next
            
        
        return linked_list == list(reversed(linked_list))