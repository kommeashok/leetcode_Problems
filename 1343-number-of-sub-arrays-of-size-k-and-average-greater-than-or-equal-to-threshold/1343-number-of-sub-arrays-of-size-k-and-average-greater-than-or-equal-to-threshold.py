class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        # window = sum(arr[:k])
        # count =0
        # for i in range(k,len(arr)):
        #     window+=arr[i]-arr[i-k]
        #     res = window/k
        #     if res>=threshold:
        #         count+=1
        # return count
        left = 0
        window = 0
        count = 0
        for i in range(0,len(arr)):
            window+=arr[i]
            if i-left+1==k:
                res = window/k
                window-=arr[left]
                left+=1 
                if res>=threshold:
                    count+=1
                    
        return count
            
            
        