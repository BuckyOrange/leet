class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        plusone = False
        newl = ListNode()
        tmp = newl
        while (l1 != None) or (l2 != None):
            if l1 == None and plusone:
                nodev = l2.val + 1
                l2 = l2.next
                plusone = False
            elif l2 == None and plusone:
                nodev = l1.val + 1
                l1 = l1.next
                plusone = False
            elif l1 == None:
                nodev = l2.val
                l2 = l2.next
            elif l2 == None:
                nodev = l1.val
                l1 = l1.next
            elif plusone:
                nodev = l1.val + l2.val + 1
                plusone = False
                l1 = l1.next
                l2 = l2.next
            else:
                nodev = l1.val + l2.val
                plusone = False
                l1 = l1.next
                l2 = l2.next

            if nodev > 9:
                plusone = True
                newl.val = nodev % 10

            else:
                newl.val = nodev

            if (l1 != None) or (l2 != None) or (plusone == True):
                newl.next = ListNode()
                newl = newl.next
            else:
                newl.next = None
                newl = newl.next
        if plusone == True:
            newl.val = 1
        return tmp