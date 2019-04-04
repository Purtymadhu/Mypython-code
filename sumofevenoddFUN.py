def evenodd(l):
    enum=[]
    for n in l:
        if n %2 ==0:
             enum.append(n)
    s=sum(enum)
    return s
arr=[int(x) for x in input("enter array elements").split(",")]
print(evenodd(arr))
