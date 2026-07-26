class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            result = len(str(i))
            if result%2==0:
                count+=1
        return count
        