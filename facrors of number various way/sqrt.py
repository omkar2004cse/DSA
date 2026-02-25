# find the factors of any number by the squreroot 
from math import sqrt as sq
num=int(input("enter a Number:-"))
r=[]
for i in range(1,(int(sq(num))+1)):
    if num%i==0:
        r.append(i)
        r.append(num//i)
r=set(r)
r=list(r)
r.sort()
print(r)