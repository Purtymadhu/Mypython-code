month=input("enter a month")
L1 = ['april','june','sep','nov']
L2 = ['jan','march','may','july','aug','octo','dec']
if month=="febuarary":
    print("28 or 29 days")
elif month in L1:
    print("30 days")
elif month in L2:
    print("31 days")
else:
    print("invalid month number")
