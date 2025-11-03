class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fast_pow(y, p):
            if p == 0:
                return 1.0
            half = fast_pow(y, p // 2)
            if p % 2 == 0:
                return half * half
            else:
                return half * half * y

        if n < 0:
            x = 1 / x
            n = -n
        return fast_pow(x, n)
