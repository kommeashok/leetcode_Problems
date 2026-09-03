class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # total = 0
        # current_total = []
        # for i in nums:
        #     total+=i
        #     current_total+= [total]
        # return current_total
        s = 0
        result = []

        for i in range(0,len(nums)):
            s+=nums[i]
            result+=[s]
        return result
            
            
            
            
        
        