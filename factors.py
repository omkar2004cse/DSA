# factor of any number
num=int(input("Enter a Number:-"))
n=num
l=[]
for i in range(1,n+1):
    if(n%i==0):
        l.append(i)
    

print(f'Factors of {num} is:-{l}')