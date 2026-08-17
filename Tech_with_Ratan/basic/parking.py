# check the parking is free or paid 
# condition are 1) age <=12  2)cycle is eligible other is not eligible

age=int(input("Enter a Your Age:-"))
if age<=18 or age >60:
    print("Parking is free")
else:
    print("Pay 50 Rs. of Parking")
