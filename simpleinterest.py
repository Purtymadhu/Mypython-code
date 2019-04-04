principle = float(input("enter a profit"))
rate= float(input("enter a rate"))
time= float(input("enter a time"))
SI= principle*rate*time/100 #simple interest for a year
print("simple interest for an year", SI)
SIM= (principle*rate*time)/(100*time*12); #simple interest for a month
print("simple interest for a month", SIM)
