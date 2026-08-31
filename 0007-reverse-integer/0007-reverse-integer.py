class Solution:
    def reverse(self, x: int) -> int:
        # if x2147483647:
        #     return 0
        # negative = 0
        num = abs(x)
        count = 0
        while num>0:
            last = num % 10
            num = num // 10
            count = count * 10 + last
            # num = num // 10
        # return count
        if x<0:
            count = -count

        if count<=-2**31 or count>=(2**31)-1:
            return 0

        return count 






        