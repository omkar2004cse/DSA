# WAP to check the person is eligible for loan or not
# criteria is:- person age is greater than 18 and its income is greater than 30000

name=input("Enter Your Name:-")
age=int(input("Enter a Your age:-"))
income=int(input("Give me input your monthly Salary:-"))

if age>18 and income>=30000:
    print(name,"you are eligible for the Loan")
else:
    print(name,"you are not eligible for the loan")