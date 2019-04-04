n=int(input("enter a number"))
x=n+1 
while True:
    for i in range(2,x):
        if x%i==0:
            break
    else:
        print("next prime number is",x)
        break
    x=x+1
