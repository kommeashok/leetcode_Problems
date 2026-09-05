class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        s = 0
        length = len(nums)
        found = False
        while right<len(nums):
            s+=nums[right] 
            while s>=target:
                found = True
                length = min(length,right-left+1)
                s-=nums[left]
                # length = min(length,right-left+1)
                left+=1
            right+=1
                
        if found==False:
            # found = True
            return 0
        return length
       