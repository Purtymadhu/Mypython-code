n=int(input("enter a number"))
m=1
for x in range(1,n,2):
    print(x,end=',')
    m=m*x
print("product of 1st odd number", m)
