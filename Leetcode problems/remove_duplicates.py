nums = [0,0,1,1,1,2,2,3,3,4]
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
def removeDuplicates(nums):
    i = 0 
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i+=1
            nums[i] = nums[j]
    return i+1

print(removeDuplicates(nums))