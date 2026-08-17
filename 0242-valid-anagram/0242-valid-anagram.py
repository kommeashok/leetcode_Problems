class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s,t = list(s),list(t)
        # s.sort()
        # t.sort()
        # if s==t:
        #     return True
        # else:
        #     return False
        
        count = {}
        for ch in s:
            if ch in count:
                count[ch]+=1
            else:
                count[ch]=1
        for ch in t:
            if ch in count:
                count[ch]-=1
            else:
                count[ch]=-1
        for ch in count:
            if count[ch]!=0:
                return False
                break 
        else:
            return True

        