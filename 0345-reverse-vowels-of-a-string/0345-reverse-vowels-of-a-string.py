class Solution:
    def reverseVowels(self, s: str) -> str:
        arr = list(s)
        left = 0
        right = len(arr)-1
        while left<right:
            if arr[left] not in "AEIOUaeiou":
                left+=1
            elif arr[right] not in "AEIOUaeiou":
                right-=1
            elif arr[left] and arr[right] in "AEIOUaeiou":
                arr[left],arr[right] = arr[right],arr[left]
                left+=1
                right-=1

        return ''.join(arr)
             
        