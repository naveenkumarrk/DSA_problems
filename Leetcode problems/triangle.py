# https://leetcode.com/problems/type-of-triangle/description/
nums = [3,2,1]

def triangleType(nums):
    nums.sort()
    if nums[0] + nums[1] <= nums[2]:
        return "none"
    if len(set(nums)) == 1:
        return 'equilateral'
    if len(set(nums)) == 2:
        return 'isosceles'
    return 'scalene'

print(triangleType(nums))