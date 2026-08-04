class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:

        nums = set(nums)
        mini = min(nums)
        maxi = max(nums)

        result = []
        
        for i in range(mini,maxi+1):
            if i not in nums:
                result+=[i]
        return result


        