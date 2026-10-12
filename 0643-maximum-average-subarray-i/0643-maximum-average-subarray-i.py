class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        if len(nums)<k:
            return nums[0]
        # left = 0
        window_sum = sum(nums[:k])
        maximum = window_sum
        for i in range(k,len(nums)):
            window_sum+=nums[i] - nums[i-k]
            maximum = max(maximum,window_sum)
            # if i-left+1==k:
            #     maximum = max(maximum,window_sum)
                # window_sum-=nums[left]
                # left+=1
            

        return maximum/k


        




