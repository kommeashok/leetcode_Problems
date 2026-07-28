class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        powerof5 = 5
        while n>=powerof5:
            result = result + n//powerof5
            powerof5 = powerof5 * 5
        return result