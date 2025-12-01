# https://leetcode.com/problems/climbing-stairs/description/
import math


class Solution:
    def climbStairs(self, n: int) -> int:
        num_of_2 = n//2
        ways = 0
        for i in range(0, num_of_2+1):
            pos = n - i
            ways += math.factorial(pos)//(math.factorial(i)
                                          * math.factorial(pos-i))
        return ways
