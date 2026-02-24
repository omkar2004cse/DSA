"""
1
22
333
4444
55555
"""
r=int(input("Enter a No of Row:-"))
for i in range (1,r+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()