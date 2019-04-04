x,y=eval(input("Enter two number"))
if y==0:
    raise ZeroDivisionError("denominator cannt be zero")
z=x/y
print("division is",z)
