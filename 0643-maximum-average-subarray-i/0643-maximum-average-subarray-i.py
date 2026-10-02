class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window = 0
        for i in range(k):
            window+=nums[i]
        maximum = window

        left = 0
        right = k-1

        while right<len(nums)-1:
            window = window - nums[left]+nums[right+1]
            maximum = max(maximum,window)
            left+=1
            right+=1
        return maximum/k