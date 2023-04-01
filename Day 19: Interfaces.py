class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        return divisors(n)
    
    
def divisors(n):
    c = 1
    s = 0
    while c <= n:
        if n % c == 0:
            s += c
        c += 1
    return s
