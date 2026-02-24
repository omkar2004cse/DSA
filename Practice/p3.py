"""
1
12
123
1234
12345
"""
r=int(input("Enter a Row:-"))
for i in range(1,r+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()