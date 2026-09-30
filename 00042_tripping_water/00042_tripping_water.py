from typing import List


def trap(height: List[int]) -> int:

    maxima = [0 for x in range(len(height))]
    maxVal = -10**10
    max_index = None
    ## this loop ensure that if we are on some index and looking on elements from index to end we always find on maxima[that_index] maximum of that subarray
    for i in range(0,len(height)):
        curr_index = len(height) - 1 - i 
        curr_val = height[curr_index]
        if(maxVal < curr_val):
            maxVal= curr_val
            max_index = curr_index

        maxima[curr_index] = (maxVal,max_index)

    #print(maxima)
    if len(height) < 3:
        return 0
    left = 0
    right = len(height)
    water = 0
    right_max,right_index = maxima[0]
    left_max = height[left]
    if right_index == 0:
        right_max,right_index = maxima[1]
    left_max = min(left_max,right_max)
    left += 1
    while left < right:
        curr_height = height[left]
        # we add water only if the current height is less than the left_max, because the water can only be put to empty blocks
        water += max(0,left_max-curr_height)
        # left_max is always maximum from height we already seen
        left_max = max(left_max,height[left])
        right_max,right_index = maxima[left]
        if (right_index == left):
            if left+1 == len(height):
                break
            right_max,right_index = maxima[left+1]
        # we updated the right_max so left can be atmost the height of right_max
        left_max = min(left_max,right_max)
        left +=1
    return water

        


height = [4, 2, 0, 3, 2, 5]

print(trap(height))
         




