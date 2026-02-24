number=int(input("Enter a Number:-"))
num=number
r_num=0
while num>0:
    last_digit=num%10
    r_num=r_num*10+last_digit
    num=int(num/10)

print(r_num)
print(type(r_num))