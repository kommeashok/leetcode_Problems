class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        i = 1
        while k>0:
            n= k*i
            if n not in nums:
                return n
                # break
            i+=1
        