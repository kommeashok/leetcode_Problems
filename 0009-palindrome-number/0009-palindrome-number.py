class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        reverse = 0
        original = x
        while original>0:
            digit = original%10
            reverse=reverse*10+digit
            original=original//10
        return x == reverse
            
        
        
        



        