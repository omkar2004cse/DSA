# parking is free or paid
# criteria :- age is less than 12 and age is greater than 60

age=int(input("Enter a your age:-"))
if age >60 or age<12:
    print("Parking is Free")
else:
    print("Parking is Paid")