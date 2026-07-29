# Definition for singly-linked list.
from ast import List

from pyparsing import Optional


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        
#nodes = []


# --- Helper functions to build and print the linked lists ---
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def to_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def to_python_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# ==========================================
# 1. Standard Case with Negatives & Duplicates
# Expected Output: [-10, -5, 0, 1, 2, 3, 5, 5, 9, 10, 11]
case_1 = [
    to_linked_list([-10, 0, 5, 9]),
    to_linked_list([-5, 1, 5, 10]),
    to_linked_list([2, 3, 11])
]

# 2. Unevenly Distributed Lists (One massive list, others short)
# Expected Output: [1, 2, 3, 4, 5, 6, 7, 8, 100, 200]
case_2 = [
    to_linked_list([1]),
    to_linked_list([100,105,108,205,208,250]),
    to_linked_list([200,205,207,209])
]

# 3. Interleaved Sequential Values
# Expected Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
case_3 = [
    to_linked_list([1, 4, 7]),
    to_linked_list([2, 5, 8]),
    to_linked_list([3, 6, 9])
]

# 4. Mixed Empty Lists and Heavy Duplication
# Expected Output: [2, 2, 2, 2, 5, 5]
case_4 = [
    to_linked_list([]),
    to_linked_list([2, 2, 5]),
    None,  # Same as an empty list node
    to_linked_list([2, 2, 5])
]

# 5. Single Element Lists (Tests heap/pointer tie-breakers)
# Expected Output: [1, 1, 2, 3, 3]
case_5 = [
    to_linked_list([-9,-3]),
    to_linked_list([-5]),
    to_linked_list([4]),
    to_linked_list([-8]),
    #to_linked_list([]),
    to_linked_list([-9]),
    to_linked_list([-3])
]

class Heap:
    def __init__(self,heapList,root):
        self.heapList = heapList
        if root != None:
            self.heapList.append(root)
        #self.firstEmpty = 2 # indexing from 1
    def add(self,value):
        if value == None:
            return
        self.heapList.append(value)
        parentIndex = len(self.heapList)//2
        if self.heapList[parentIndex-1][0] > value[0]:
            currNode = len(self.heapList)
            while currNode > 1 and self.heapList[parentIndex-1][0] > self.heapList[currNode-1][0]:
                ## we swap them because it violate heap condition
                self.heapList[parentIndex-1],self.heapList[currNode-1] = self.heapList[currNode-1], self.heapList[parentIndex-1] 
                currNode = parentIndex
                parentIndex = currNode // 2
    def remove(self):
        minValue = self.heapList[0]
        self.heapList[0] = self.heapList[-1]
        self.heapList.pop()

        currNode = 1
        children1 = currNode*2
        children2 = currNode*(2+1) 
        if children1 > len(self.heapList):
            currNode = len(self.heapList) + 1
        child1_val = float('inf') if children1 > len(self.heapList) else self.heapList[children1-1][0]
        child2_val = float('inf') if children2 > len(self.heapList) else self.heapList[children2-1][0]
        while currNode <= len(self.heapList) and (self.heapList[currNode-1][0] > child1_val or self.heapList[currNode-1][0] > child2_val):
            if child1_val < child2_val:
                self.heapList[currNode-1],self.heapList[children1-1] = self.heapList[children1-1],self.heapList[currNode-1]
                currNode = children1
            else:
                self.heapList[currNode-1],self.heapList[children2-1] = self.heapList[children2-1],self.heapList[currNode-1]
                currNode = children2
            children1 = currNode*2
            children2 = currNode*2+1
            child1_val = float('inf') if children1 > len(self.heapList) else self.heapList[children1-1][0]
            child2_val = float('inf') if children2 > len(self.heapList) else self.heapList[children2-1][0]
        return minValue
            



def mergeKLists(lists):
    merged = []
    if lists[0] != None:
        H = Heap([], (lists[0].val, 0))
    else:
        H = Heap([], None)
    for i in range(1,len(lists)):
        if lists[i] != None:
            H.add((lists[i].val, i))
    while (len(H.heapList) > 0):
        val,k_list = H.remove()
        merged.append(val)
        lists[k_list] = lists[k_list].next
        if (lists[k_list] != None):
            H.add((lists[k_list].val,k_list))
    print(merged)
        

mergeKLists(case_5)




















# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Heap:
#     def __init__(self,heapList,root):
#         self.heapList = heapList
#         if root != None:
#             self.heapList.append(root)
#         #self.firstEmpty = 2 # indexing from 1
#     def add(self,value):
#         if value == None:
#             return
#         self.heapList.append(value)
#         parentIndex = len(self.heapList)//2
#         if self.heapList[parentIndex-1][0] > value[0]:
#             currNode = len(self.heapList)
#             while currNode > 1 and self.heapList[parentIndex-1][0] > self.heapList[currNode-1][0]:
#                 ## we swap them because it violate heap condition
#                 self.heapList[parentIndex-1],self.heapList[currNode-1] = self.heapList[currNode-1], self.heapList[parentIndex-1] 
#                 currNode = parentIndex
#                 parentIndex = currNode // 2
#     def remove(self):
#         minValue = self.heapList[0]
#         self.heapList[0] = self.heapList[-1]
#         self.heapList.pop()

#         currNode = 1
#         children1 = currNode*2
#         children2 = currNode*(2+1) 
#         if children1 > len(self.heapList):
#             currNode = len(self.heapList) + 1
#         child1_val = float('inf') if children1 > len(self.heapList) else self.heapList[children1-1][0]
#         child2_val = float('inf') if children2 > len(self.heapList) else self.heapList[children2-1][0]
#         while currNode <= len(self.heapList) and (self.heapList[currNode-1][0] > child1_val or self.heapList[currNode-1][0] > child2_val):
#             if child1_val < child2_val:
#                 self.heapList[currNode-1],self.heapList[children1-1] = self.heapList[children1-1],self.heapList[currNode-1]
#                 currNode = children1
#             else:
#                 self.heapList[currNode-1],self.heapList[children2-1] = self.heapList[children2-1],self.heapList[currNode-1]
#                 currNode = children2
#             children1 = currNode*2
#             children2 = currNode*(2+1)
#             child1_val = float('inf') if children1 > len(self.heapList) else self.heapList[children1-1][0]
#             child2_val = float('inf') if children2 > len(self.heapList) else self.heapList[children2-1][0]
#         return minValue
            

# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         dummy = ListNode(0)
#         tail = dummy
#         merged = []
#         if len(lists) == 0:
#             return None
#         if lists[0] != None:
#             H = Heap([], (lists[0].val, 0))
#         else:
#             H = Heap([], None)
#         for i in range(1,len(lists)):
#             if lists[i] != None:
#                 H.add((lists[i].val, i))
#         while (len(H.heapList) > 0):
#             val,k_list = H.remove()
#             merged.append(val)
#             tail.next = ListNode(val)
#             tail = tail.next

#             lists[k_list] = lists[k_list].next
#             if (lists[k_list] != None):
#                 H.add((lists[k_list].val,k_list))

#         return dummy.next