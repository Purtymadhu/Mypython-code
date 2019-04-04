values=tuple(int(x) for x in input("enter tuple elements").split(','))
l=[]
for i in values:
    l+=[i]
    i=i+1
print(l)
l.sort()
print("sorted values are",l)

