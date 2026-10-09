class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        result = []
        for i in range(0,len(nums)):
            store = nums[i]*nums[i]
            result.append(store)
            result.sort()
        return result
        