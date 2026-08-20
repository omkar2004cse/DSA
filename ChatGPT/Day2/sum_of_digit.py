# Take an integer and calculate the sum of its digits.

number=int(input("Enter a Number:-"))
tem=number
s=0
while tem > 0:
    digi=tem%10
    s=s+digi
    tem=tem//10

print("sum of digit of",number,"is:-",s)