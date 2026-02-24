num=int(input("Enter a number:-"))
n=num
r_num=0
while n>0:
    last_d=n%10
    r_num=r_num*10+last_d
    n=n//10

if num==r_num:
    print(num,"and",r_num,"is Plaindrom")
else:
    print(num,"and",r_num,"is not Plaindrom")