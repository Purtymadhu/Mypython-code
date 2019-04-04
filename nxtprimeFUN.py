def nxtprime(num):
    x=num+1
    while True:
        for i in range(2,x):
            if x % i==0:
                break
        else:
            return x
        x=x+1;
print("enter a number")
n=int(input())
print("next prime number of a given nubmer is",nxtprime(n))
