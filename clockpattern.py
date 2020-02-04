n=6
k=7
for i in range(n,0,-1):
    for j in range(0,k+1):
        print(end=" ")
    k=k+1
    for i in range(0,i):
        print("* ",end="")
    print("\r")
for i in range(0,n):
    for j in range(0,k):
        print(end=" ")
    k=k-1
    for i in range(0,i+1):
        print("* ",end="")
    print("\r")

