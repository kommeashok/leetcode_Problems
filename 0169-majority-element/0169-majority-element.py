class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # for i in range(0,len(nums)):
        #     count = 0
        #     for j in range(0,len(nums)):
        #         if nums[i]==nums[j]:
        #             count+=1
        #     if count>len(nums)//2:
        #         return nums[i]
        dictionary = {}
        for i in range(0,len(nums)):
            if nums[i] not in dictionary:
                dictionary[nums[i]]=1
            else:
                dictionary[nums[i]]+=1
        for key,value in dictionary.items():
            if value>len(nums)//2:
                return key
