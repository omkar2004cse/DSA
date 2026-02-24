"""
12345
1234
123
12
1
"""
r=int(input("Enter a No of Row:-"))
for i in range(r):
    for j in range(1,r-i+1):
        print(j,end=" ")
    print()