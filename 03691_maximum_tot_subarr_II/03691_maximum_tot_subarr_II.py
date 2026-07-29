from typing import List
import heapq


### LEFT LOWEST, RIGHT HIGHEST
def findSol(leftB,rightB,nums_heap,nums_neg_heap)
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:

        #nums_with_indices = []
        nums_heap = nums.copy()
        nums_neg_heap = [-x for x in nums_heap]
        heapq.heapify(nums_heap)
        heapq.heapify(nums_neg_heap)
        
        rangeTable = {}

      
        ### FOR K
        out_left = 0
        out_right = len(nums) - 1
        i = k
        result = 0
            
            


            
