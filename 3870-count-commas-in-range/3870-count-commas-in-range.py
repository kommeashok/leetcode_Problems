class Solution:
    def countCommas(self, n: int) -> int:
        # if n<1000:
        #     return 0
        count = 0
        for i in range(n,999,-1):
            count+=1
        return count
        