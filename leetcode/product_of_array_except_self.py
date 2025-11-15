from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int])->List[int]:
        
        prefix_product=[None]*len(nums)
        suffix_product=[None]*len(nums)

        for i in range(len(nums)):
            if(i>1):
                prefix_product[i]=prefix_product[i-1]*nums[i-1]

            if(i==1):
                prefix_product[i] = nums[i-1]

            nums_length = len(nums)-1
        for i in range(nums_length,-1,-1):
            if(i==nums_length-1):
                suffix_product[i]=nums[i+1]
            if(i<nums_length-1):
                suffix_product[i]=suffix_product[i+1]*nums[i+1]

        for i in range(len(nums)):
            if(i==0):
                nums[i]=suffix_product[i]
            elif(i==nums_length):
                nums[i]=prefix_product[i]
            else:
                nums[i]=prefix_product[i]*suffix_product[i]

        return nums



sol = Solution()

print(sol.productExceptSelf([-1,1,0,-3,3]))
