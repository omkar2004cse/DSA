num=int(input("Enter a Number as the Input:-"))
n=num
count=0
while n>0:
    last_digit=n%10
    print(last_digit)
    count+=1
    n=int(n/10)

print(f'count of digit in number is:{count}')