from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def fromList(arr):
        tmp = None
        for val in reversed(arr):
            tmp = ListNode(val, tmp)
        return tmp
    
    def __str__(self):
        curr = self
        ret = "["
        while curr != None:
            ret += f"{curr.val}, "
            curr = curr.next
        return ret[:-2] + "]"
        
class Solution:
    # reverse in place
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev
    
    # https://leetcode.com/problems/remove-nodes-from-linked-list/
    # Remove every node which has a node with a greater value anywhere to the right side of it.
    # reverses in place
    def removeNodes_InPlace(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # reverse the list
        prev = self.reverseList(head)
        # traverse the reversed list to find nodes that satisfy removal condition
        fake_head = ListNode()
        prev, curr = fake_head, prev
        while curr:
            if curr.val >= prev.val:
                prev.next = curr
                prev = prev.next
            tmp = curr
            curr = curr.next
            tmp.next = None
        # reverse the list again
        prev = self.reverseList(fake_head.next)
        return prev
    
    # https://leetcode.com/problems/remove-nodes-from-linked-list/
    # Remove every node which has a node with a greater value anywhere to the right side of it.
    # original idea with a list to keep reversed nodes
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr = head
        while curr != None:
            arr.append(curr)
            curr = curr.next
        max_val = 0
        nxt = None
        for node in reversed(arr):
            if node.val >= max_val:
                max_val = node.val
                nxt = ListNode(node.val, nxt)
        return nxt
    
    # https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/
    #  Swap the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed)
    def swapNodes_List(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        arr[k-1], arr[-k] = arr[-k], arr[k-1]
        curr = head
        i = 0
        while curr:
            curr.val = arr[i]
            curr = curr.next
            i += 1
        return head

    # in-place, doesn't need a list
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first = last = head
        for i in range(k-1):
            first = first.next
        # use end as a measuring stick - when end finishes, last is at the -kth position
        end = first
        while end.next:
            last = last.next
            end = end.next
        first.val, last.val = last.val, first.val
        return head

    # merge for MergeSort
    def merge(self, head1, head2):
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

    # regular degular sort, but was from leetcode
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
    
    # https://neetcode.io/problems/reorder-linked-list/question?list=blind75
    '''
    You are given the head of a singly linked-list.
    The positions of a linked list of length = 7 for example, can intially be represented as:
        [0, 1, 2, 3, 4, 5, 6]
    Reorder the nodes of the linked list to be in the following order:
        [0, 6, 1, 5, 2, 4, 3]
    Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:
    [0, n-1, 1, n-2, 2, n-3, ...]
    You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.
    '''
    def reorderList(self, head: Optional[ListNode]) -> None:
        # get the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse the second half
        curr = slow.next
        prev = slow.next = None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        # now interweave forward and reverse
        fr, rv = head, prev
        while rv:
            next_fr, next_rv = fr.next, rv.next
            fr.next, rv.next = rv, next_fr
            fr, rv = next_fr, next_rv
        return head

if __name__=='__main__':
    print("reorder list method")
    arr = [2,4,6,8]
    print(arr)
    print(Solution().reorderList(ListNode.fromList(arr)))
    arr = [2,4,6,8,10]
    print(arr)
    print(Solution().reorderList(ListNode.fromList(arr)))
    
    # print("Remove method")
    # arr = [5,2,13,3,8]
    # print(arr)
    # print(Solution().removeNodes(ListNode.fromList(arr)))
    
    # print("Swap method")
    # arr = [7,9,6,6,7,8,3,0,9,5]
    # print(arr)
    # print(Solution().swapNodes(ListNode.fromList(arr), 5))
    # arr = [1,2,3,4,5]
    # print(arr)
    # print(Solution().swapNodes(ListNode.fromList(arr), 2))
    