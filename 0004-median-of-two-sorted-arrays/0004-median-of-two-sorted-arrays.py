class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = nums1+nums2
        result.sort()
        length = len(result)
        if length%2==1:
            # res = (length+1)/2
            return result[length//2]
    
    # print(res/2)
        else:
            res1 = result[length // 2 - 1]
            res2 = result[length // 2]
            return (res1 + res2) / 2
