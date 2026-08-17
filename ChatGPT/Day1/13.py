# Simple Calculator
print("** Welcome in Simple Calculator")
num1=int(input("Enter a Frist Number:-"))
num2=int(input("Enter a Second Number:-"))

print("Choose Option\na)Addition\nb)Substraction\nc)Multiplication\nd)Division\ne)Reminder\nf)Square\ng)Floor Division\n('Note Give only option character( for ex:- a or b)')")

option=input("Enter Your Option:-").lower()
if option=="a":
    print("Addition of",num1,"and",num2,"is:-",num1+num2)
elif option=='b':
    print("Substraction of",num1,"and",num2,"is:-",num1-num2)
elif option=='c':
    print("Multiplication of",num1,"and",num2,"is:-",num1*num2)
elif option=='d':
    print("Division of",num1,"and",num2,"is:-",num1/num2)
elif option=='e':
    print("Reminder of Division",num1,"and",num2,"is:-",num1%num2)
elif option=='f':
    print("Square of",num1,"and",num2,"is:-",num1**2,num2**2)
elif option=='g':
    print("Floor Division of",num1,"and",num2,"is:-",num1//num2)
else:
    print("Your Option is Wrong\nPlease Try Later")