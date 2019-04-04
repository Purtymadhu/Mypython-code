def sumf(n):
    if n==1:
        return 1
    return n**2+sumf(n-1)
