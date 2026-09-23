# Definition for singly-linked list.
import math
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def lenList(self, head):
        i = 0
        while head != None:
            i += 1
            head = head.next
        return i
    def reverseInSide(self,head,i):
        a = head
        b = a.next
        c = b.next
        while i > 0:
            "a->b->c->d"
            b.next = a
            "a<->b c->d"
            i -= 1

            a = b
            b = c 
            if (c != None):
                c = c.next           
        return a,b
            
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        leftBound = head
        leftBoundPrev = None
        rightBound = head
        numElements = self.lenList(head)
        #numSegments = math.ceil(numElements / k)
        numSegments = numElements // k
        if k == 1:
            return head
        i = 0
        for j in range(numSegments):
            ## we do switches
            rightBound, rightBoundNext = self.reverseInSide(leftBound,min(k-1,numElements-i-1))
            i+=k
            ## now we now leftBound and rightBound and their neighbours so we can switch it
            ## leftBoundPrev leftBound xxx rightBound rightBoundNext
            ## we want leftBoundPRev -> rightBound xxx leftBound -> rightBoundNext
            leftBound.next = rightBoundNext
            if (leftBoundPrev != None):
                leftBoundPrev.next = rightBound
            ## now we move it
            leftBoundPrev = leftBound
            leftBound = rightBoundNext


            if (j == 0):
                head = rightBound
        return head

#### leftBoundPrev leftBound leftBound.next xxx prevPrevHead prevHead currentHead currentHead.next rightBound rightBound.next 







# case1
def addVals(vals):
    root = ListNode(vals[0])
    head = root
    for v in vals[1:]:
        head.next = ListNode(v)
        head = head.next
    return root
#vals = [1,2,3,4,5,6]
head = [1, 2, 3, 4, 5]
k = 2
a = addVals(head)
sol = Solution()
head = sol.reverseKGroup(a,k=k)
print(sol.printList(head))