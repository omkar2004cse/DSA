# Find the largest of three numbers.
a=int(input("Enter a Frist Number:="))
b=int(input("Enter a Second Number:="))
c=int(input("Enter a Third Number:="))

if a>b:
    if a>c:
        print(a,'is greater than',b,c)
    else:
        print(c,'is greater than',a,b)
else:
    if b>c:
        print(b,'is greater than',a,c)
    else:
        print(c,'is greater than',a,b)



print(id(a))