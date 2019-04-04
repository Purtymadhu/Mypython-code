def avg(*n):
    s=0
    for x in n:
        s=s+x
        return s//len(n)
x=tuple(input("enter values"))
print("average of values",avg(x))
