class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n = len(nums)
        # expected_sum = 0
        # actual_sum = int(n * (n+1)/2)
        # for i in nums:
        #     expected_sum+=i
        # return actual_sum  - expected_sum 
        xor1 = 0
        for i in range(len(nums)+1):
            xor1 = xor1^i
        xor2 = 0
        for i in nums:
            xor2 = xor2^i
        return xor1^xor2