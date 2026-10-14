class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        nums.sort()
        left = 0
        ans = float("inf")
        for i in range(0,len(nums)):
            if i-left==k:
                left+=1
            if i-left+1==k:
                ans = min(ans,nums[i]-nums[left])
        return ans

        