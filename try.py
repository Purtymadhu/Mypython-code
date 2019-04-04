x=int(input("enter a number"))
s=0;
for i in range(1,x,2):
    print(i,end=',')
    s=s+i;
print("sum of first odd natural no", s)
