# https://leetcode.com/problems/fibonacci-number/description/
class Solution:
    def fib(self, n: int) -> int:
        fib_0 = 0
        fib_1 = 1
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            i = 2
            while (i <= n):
                fib_2 = fib_1+fib_0
                fib_0 = fib_1
                fib_1 = fib_2
                i += 1
            return fib_2
