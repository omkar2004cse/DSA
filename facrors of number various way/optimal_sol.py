# find the factors of number is complete the divisible
# the factors of any number is upto the half of the number and then the last number
"""
10 
1-yes
2-yes
3-no
4-no
5-yes
6,7,8,9-no
10- yes
"""
number=int(input("Enter a number to get the factors:-"))
result=[]
for i in range(1,number//2+1):
    if(number%i==0):
        result.append(i)
result.append(number)
print(f'Factors of {number} is:-',result)