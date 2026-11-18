class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # left = 1
        # for i in range(1,len(nums)):
        #     if nums[i]!=nums[left-1]:
        #         nums[left] = nums[i]
        #         left+=1
        # return nums[:left]
        # nums.sort()
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i+=1
                nums[i]=nums[j]
        return i+1
            
            
        