# amstrong number
number=int(input("Enter a Number:-"))
n=number
result=0
p=len(str(n))
while n>0:
    l_digit=n%10
    result+=l_digit ** p
    n=n//10


if number==result:
    print(f'{number} is Plaindrom')
else:
    print(f"{number} is not Plaindrom")