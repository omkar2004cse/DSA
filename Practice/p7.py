"""
    *
   * *
  * * *
* * * * *
"""
r=int(input("Enter a No of Row:-"))
for i in range(r):
    for j in range(r-i):
        print("",end=" ")
    for k in range(0,i+1):
        print("* ",end="")
    print()