class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(c**0.5)
        total = 0
      
        while left<=right:
            total = left*left + right*right
            if total<c:
                left+=1
            elif total>c:
                right-=1
            elif total==c:
                return True
        return False
            