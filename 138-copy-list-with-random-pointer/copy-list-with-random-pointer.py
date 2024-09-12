"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        if not head:
            return None
        
        hash = {}
        
        curr = head
        while curr:
            hash[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            if curr.next:
                hash[curr].next = hash[curr.next]
            if curr.random:
                hash[curr].random = hash[curr.random]
            curr = curr.next
            
        return hash[head]