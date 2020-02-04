n=5
k=5
for i in range(0,n):
    for j in range(0,k):
        if i+j==2 or i-j==2 or i+j==6 or j-i==2:
            print("*",end=" ")
        else:
            print(end=" ")
    print()
