class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        duplicates = []
        for i in nums:
            if i in seen:
                duplicates.append(i)
            else:
                seen.add(i)
        length = len(duplicates)
        if length>0:
            return True
        else:
            return False
            
        