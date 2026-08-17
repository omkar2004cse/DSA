# Swap two numbers using a third variable.

num1=int(input("Enter a Frist Number:-"))
num2=int(input("Enter a Second Number:-"))
print("Befor Swaping    ",num1,'\t',num2)
# num3=num2
# num2=num1
# num1=num3

# print("After Swaping    ",num1,'\t',num2)

# Swap two numbers without using a third variable.
num1=num1+num2
num2=num1-num2
num1=num1-num2

print("After Swaping    ",num1,'\t',num2)