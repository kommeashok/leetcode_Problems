class Solution:
    def checkDivisibility(self, n: int) -> bool:
        add = 0
        multiply = 1
        for i in str(n):
            i = int(i)
            add+=i
            multiply*=i
        total = add+multiply
        if n%total ==0:
            return True
        else:
            return False
        