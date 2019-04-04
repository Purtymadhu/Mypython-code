val=tuple(int(x) for x in input("Enter tuples elements").split(','))
val2=tuple(int(x) for x in input("Enter tuples elements").split(','))
if set(val)==set(val2):
    print("elements  are same in both tuples")
else:
    print("elements are not same in both tuples")
