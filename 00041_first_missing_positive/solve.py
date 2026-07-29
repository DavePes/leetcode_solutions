
from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1,n+1):
            num = nums[i-1]
            while (num > 0 and num <= n and nums[num-1] != num):
                ## we do switch
                nums[i-1],nums[num-1] = nums[num-1],num
                num = nums[i-1]

        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1

A = Solution()
tests = [
    ([1,1,2,2,4], 3), ([1,100,2,200], 3)
]

for nums, exp in tests:
    res = A.firstMissingPositive(list(nums))
    print(f"{'✓' if res == exp else '✗'} In: {nums} | Out: {res} (Exp: {exp})")