nums = [(x,x+5) for x in range(0,20)]
nums = [(0, 5), (1, 6), (2, 8), (3, 9)]


def binary_search(search_num,left,right,nums):

    middle = (left+right)//2
    if nums[middle][1] == search_num:
        return nums[middle]
    if left == right:
        return "not acceptable"
    if nums[middle][1] > search_num:
        if middle-1 < left:
            return "Not acceptable"
        return binary_search(search_num,left,middle-1,nums)
    if nums[middle][1] < search_num:
        return binary_search(search_num,middle+1,right,nums)
    

print(binary_search(7,0,len(nums)-1,nums))