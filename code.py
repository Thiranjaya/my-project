# Electricity bill calculation
units=int(input())
charge=0
if units<=50:
    charge=units*5
elif units<=150:
    charge=250+(units-50)*6

else:
    charge=250+700+(units-150)*10
charge=charge*1.20
print("units comsumed=",units)
print("charges=",charge)

# changes01 to master branch

# changes to master branch

