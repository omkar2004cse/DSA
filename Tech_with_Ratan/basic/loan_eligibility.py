# condition is age >=18 and income is > 50000
age=int(input("Enter a Your age:-"))
salary=int(input("Enter a Your Salary:-"))

# if (age>=18 and salary>=50000):
#     print("You are Eligible for take Loan")
# else:
#     print("You are not Eligible for Loan")

check=age>=18 and salary>=50000
print("they are eligible:-",check)