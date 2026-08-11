class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        count = ""
        for i in digits:
            count+=str(i)
        res = int(count)+1
        res = [ int(i) for i in str(res) ]
        return res
        
        