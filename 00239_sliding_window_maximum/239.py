from typing import List
import heapq

class Solution:
    def maxSlidingWindow(self,nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return None
        nums = [-x for x in nums]
        window = nums[:k]
        heapq.heapify(window)
        popped_ele = {}
        output = []
        for i in range(k,len(nums)+1):
            min = window[0]
            while popped_ele.get(min,0) != 0:
                    heapq.heappop(window)
                    popped_ele[min] -= 1
                    min = window[0]
            output.append(-min)

            ## add to popped most left element
            popped_ele[nums[i-k]] = popped_ele.get(nums[i-k],0) + 1
            if i < len(nums):
                heapq.heappush(window,nums[i])
        return output


# Test Suite
def run_tests():
    solution = Solution()
    
    test_cases = [
        {
            "name": "Standard Case",
            "nums": [1, 3, -1, -3, 5, 3, 6, 7],
            "k": 3,
            "expected": [3, 3, 5, 5, 6, 7]
        },
        {
            "name": "Strictly Decreasing",
            "nums": [9, 8, 7, 6, 5],
            "k": 2,
            "expected": [9, 8, 7, 6]
        },
        {
            "name": "Strictly Increasing",
            "nums": [1, 2, 3, 4, 5],
            "k": 3,
            "expected": [3, 4, 5]
        },
        {
            "name": "Window Equals Array Size",
            "nums": [-4, 2, -5, 3, 6],
            "k": 5,
            "expected": [6]
        },
        {
            "name": "Window Size 1",
            "nums": [4, -2, 1, 5],
            "k": 1,
            "expected": [4, -2, 1, 5]
        },
        {
            "name": "Duplicates and Varying Peaks",
            "nums": [7, 2, 4, 4, 4, 2, 7],
            "k": 3,
            "expected": [7, 4, 4, 4, 7]
        },
        {
            "name": "Single Element",
            "nums": [1],
            "k": 1,
            "expected": [1]
        }
    ]

    passed = 0
    for i, tc in enumerate(test_cases, 1):
        result = solution.maxSlidingWindow(tc["nums"], tc["k"])
        if result == tc["expected"]:
            print(f"Test {i} ({tc['name']}): PASSED")
            passed += 1
        else:
            print(f"Test {i} ({tc['name']}): FAILED")
            print(f"  Input: nums={tc['nums']}, k={tc['k']}")
            print(f"  Expected: {tc['expected']}")
            print(f"  Got:      {result}")
            
    print(f"\nResult: {passed}/{len(test_cases)} tests passed.")

run_tests()