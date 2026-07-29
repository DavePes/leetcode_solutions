from typing import List
class Solution:
    def calcMedian(self,A,B,i,j,total):
        A_left = A[i] if i >= 0 else float('-inf')
        A_right = A[i+1] if (i + 1) < len(A) else float('inf')
        
        B_left = B[j] if j >= 0 else float('-inf')
        B_right = B[j+1] if (j + 1) < len(B) else float('inf')
        if (total % 2 == 1):
            return max(A_left,B_left)
        else:
            rightPartiton = [0,0]
            if len(A) != i+1:
                rightPartiton[0] = A[i+1]
            else:
                rightPartiton[0] = B[j+1]
            if len(B) != j+1:
                rightPartiton[1] = B[j+1]
            else:
                rightPartiton[1] = A[i+1]
            return (max(A_left,B_left) + min(rightPartiton))/2
    def binarySearch(self,A,B,left,right):
        total = len(A) + len(B)
        i = (left+right)//2
        j = (total+1)//2 - i - 2
        A_left = A[i] if i >= 0 else float('-inf')
        A_right = A[i+1] if (i + 1) < len(A) else float('inf')
        
        B_left = B[j] if j >= 0 else float('-inf')
        B_right = B[j+1] if (j + 1) < len(B) else float('inf')
        # basically what we want is A[i] (most right ele in B left partition) be A[i] <=  B[j+1] (most left ele in V right partition) 
        # and B[j] (most right ele in B left parittion be B[j] <= than A[i+1]) (most left ele in A right partition)
        if A_left <= B_right and B_left <= A_right:
            return self.calcMedian(A,B,i,j,total)
        # case of A too large -> go to left
        if A_left > B_right:
            return self.binarySearch(A,B,left,i-1)
        # case A is too small -> go to right
        if B_left > A_right:
            return self.binarySearch(A,B,i+1,right)
        return self.calcMedian(A,B,i,j,total)

    def findMedianTrivialCase(self, nums1, nums2):
        # Assumes ALL elements in nums1 are strictly less than ALL elements in nums2
        n1, n2 = len(nums1), len(nums2)
        total = n1 + n2
        
        def get_val(idx):
            if idx < n1:
                return nums1[idx]
            return nums2[idx - n1]
            
        ind1 = (total - 1) // 2
        ind2 = total // 2
        
        return (get_val(ind1) + get_val(ind2)) / 2.0

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        # trivial cases
        if len(nums1) == 0:
            return (nums2[n2//2] + nums2[(n2+1)//2 - 1]) / 2
        if len(nums2) == 0:
            return (nums1[n1//2] + nums1[(n1+1)//2 - 1]) / 2
        if (nums1[-1] < nums2[0]):
            return self.findMedianTrivialCase(nums1,nums2)
        if (nums2[-1] < nums1[0]):
            return self.findMedianTrivialCase(nums2,nums1)
        
        if (n1 < n2):
            return self.binarySearch(nums1, nums2, 0, n1-1)
        else:
            return self.binarySearch(nums2, nums1, 0, n2-1)
        


sol = Solution()
tricky_cases = [
    ([3], [1,2,4], 2.5),
]

for n1, n2, exp in tricky_cases:
    res = sol.findMedianSortedArrays(n1, n2)
    print(f"Got: {res} | Expected: {exp} -> {'PASSED' if res == exp else 'FAILED'}")