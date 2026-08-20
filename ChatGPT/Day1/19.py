# Leap Year
year=int(input("Enter a Year:-"))


if year%100==0:
    print("Year is Not Leap Year")
elif year%4==0 or year%400==0:
    print("Year is Leap")
else:
    print("Not Leap Year")