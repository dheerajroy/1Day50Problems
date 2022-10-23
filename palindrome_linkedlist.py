# Problem from leetcode.com

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        h = []
        while True:
            if head:
                h.append(head.val) 
            else:
                break
            head = head.next
        return h == h[::-1]
