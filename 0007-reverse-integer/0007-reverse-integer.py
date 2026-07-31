class Solution:
    def reverse(self, x: int) -> int:
        # if x2147483647:
        #     return 0
        negative = x<0
        x = abs(x)
        count = 0
        while x>0:
            last = x % 10
            count = count * 10 + last
            x = x // 10
        if negative:
            count = -1 * count

        if count >=2147483647 or count<=-2147483648:
            return 0

        return count 






        