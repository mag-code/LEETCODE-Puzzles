class Solution:
    def fib(self, n:int) -> int:
        x,y=0,1
        if n == 0:
            return x
        elif n ==1:
            return y
        for i in range(2,n+1):
            j,x=x+y,y
            y=j
        return y