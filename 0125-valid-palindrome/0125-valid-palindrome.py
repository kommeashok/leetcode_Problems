class Solution:
    def isPalindrome(self, s: str) -> bool:

        result = ""
        for ch in s:
            if ch.isalnum():
                result+=ch.lower()
        if result == result[::-1]:
            return True
        else:
            return False
        # left = 0
        # right = len(s)-1
        # while left<right:
        #     if s[left]!=s[right]:
        #         return False
        #     left+=1
        #     right-=1
        # return True
        