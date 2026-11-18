class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # count = 0
        # for i in range(0,len(nums)):
        #     if nums[i]!=val:
        #         count+=1
        # return count 

        i = 0
        for j in range(0,len(nums)):
            if nums[j]!=val:
                nums[i] = nums[j]
                i+=1
        return i

       

        