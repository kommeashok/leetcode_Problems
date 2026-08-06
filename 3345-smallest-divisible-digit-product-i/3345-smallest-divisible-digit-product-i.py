class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n,n+10):

            digit = str(i)
            product = 1
            for j in digit:
                
                num = int(j)
                product*=num
            if product % t ==0:
                return int(digit)
            