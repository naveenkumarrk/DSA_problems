# s = "1101"

# def bin_to_dec(nums):
#     dec = 0
#     n = len(nums)
#     for i in range(n):
#         dec += int(nums[i])* 2**(n - i - 1)
#     return dec 

# def even(num):
#     return num % 2

# def steps(s):
#    num = bin_to_dec(s)    
#    count = 0
#    while num != 1:    
#        if even(num):
#            num//=2
#        else:
#            num+=1
#        count+=1
       
#    return count

# print(steps(s))   
    
    
class Solution:
    def numSteps(self, s: str) -> int:
        res, carry = 0, False

        # iterate from the LSB up to, but not including the MSB
        for b in s[:0:-1]:
            if b == "1" and not carry or b == "0" and carry:
                res += 2
                carry = True
            else: # b == "1" and carry or b == "0" and not carry
                res += 1
        
        return res + int(carry)
