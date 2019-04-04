def sumcube(n):
    if n==1:
        return 1
    return n**3+sumcube(n-1)
