a=int(input("enter first numbers"))
b=int(input("enter second numbers"))
for x in range(a,b+1):
    for y in range(2,x):
        if x%y == 0:
            break
    else:
        print(x)
 
