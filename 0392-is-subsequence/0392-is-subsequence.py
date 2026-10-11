class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0
        for i in range(0,len(t)):
            if left < len(s) and s[left]==t[i]:
                left+=1
        if left==len(s):
            return True
        return False
        