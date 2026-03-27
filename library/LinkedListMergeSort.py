from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
        curr = self
        ret = "["
        while curr != None:
            ret += f"{curr.val}, "
            curr = curr.next
        return ret[:-1] + "]"

class Solution:
    # reverse in place
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev
    
    def merge(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        # base cases
        if not head1:
            return head2
        if not head2:
            return head1
        # merging two lists
        fake_head = ListNode()
        curr = fake_head
        while (head1 and head2):
            if head1.val < head2.val:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next
            curr = curr.next
        # include last node
        curr.next = head1 if head1 else head2
        return fake_head.next

    def sortList(self, head):
        # base case
        if not head or not head.next:
            return head
        # slow and fast are for splitting the list by pointers
        # when fast gets to the end, slow should be midway
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            if fast:
                slow = slow.next
        second = slow.next
        slow.next = None
        head = self.sortList(head)
        second = self.sortList(second)

        return self.merge(head, second)

if __name__=='__main__':
    arr = [4, 2, 1, 3]
    tmp = None
    for val in reversed(arr):
        tmp = ListNode(val, tmp)
    print("\n" + str(arr))
    print(Solution().sortList(tmp))
    
    arr = [-1, 5, 3, 4, 0]
    tmp = None
    for val in reversed(arr):
        tmp = ListNode(val, tmp)
    print("\n" + str(arr))
    print(Solution().sortList(tmp))