def prime(num):
    x=2
    while num:
         for i in range(2,x):
            if x %i ==0:
                break
        else:
            print(x,end=" ")
            num=num-1
        x=x+1
n=int(input("enter a number"))
prime(n)
