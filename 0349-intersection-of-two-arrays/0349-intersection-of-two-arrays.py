class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        section = []
        left = 0
        right = 0
        while left<len(nums1) and right<len(nums2):
            if nums1[left]<nums2[right]:
                left+=1
            elif nums2[right]<nums1[left]:
                right+=1
            else:
                if not section or section[-1]!=nums1[left]:
                    section.append(nums1[left])
                left+=1
                right+=1
        return section
        