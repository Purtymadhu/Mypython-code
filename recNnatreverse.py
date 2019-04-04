def recnat(n):
    if n>0:
        recnat(n-1)
        print(n[::-1],end=' ')
