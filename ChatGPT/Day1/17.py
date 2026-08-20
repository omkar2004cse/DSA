# Largest of Three Numbers

num1=int(input("Enter a Frist Number:-"))
num2=int(input("Enter a Second Number:-"))
num3=int(input("Enter a Third Number:-"))

if num1>num2:
    if num1>num3:
        print(num1,"is greater than",num2,num3)
    else:
        print(num3,'is greater than',num1,num2)
else:
    if num2>num3:
        print(num2,'is greater than',num1,num3)
    else:
        print(num3,'is greater than',num1,num2)