# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        curr = self
        ret = ""
        while (curr is not None):
            ret += str(curr.val) + " "
            curr = curr.next
        return ret
    
class Solution:
    def insertionSortList(self, head):
        curr = head.next
        head.next = None
        while curr is not None:
            prev, cmp = None, head
            # save off next for later
            nxt = curr.next
            # find position to insert curr into
            while cmp is not None and cmp != curr:
                if curr.val < cmp.val:
                    break
                prev, cmp = cmp, cmp.next
            # insert curr and go to next
            if prev is None:
                head = curr
            else:
                prev.next = curr
            curr.next = cmp
            curr = nxt
        return head

if __name__ == '__main__':
    arr = [4, 2, 1, 3][::-1]
    tmp = None
    for elem in arr:
        tmp = ListNode(elem, tmp)
    print(f"Before sorting: {tmp}")
    print(f"After sorting: {Solution().insertionSortList(tmp)}")
    arr = [-1, 5, 3, 4, 0][::-1]
    tmp = None
    for elem in arr:
        tmp = ListNode(elem, tmp)
    print(f"Before sorting: {tmp}")
    print(f"After sorting: {Solution().insertionSortList(tmp)}")