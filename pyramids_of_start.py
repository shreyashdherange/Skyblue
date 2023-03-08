n=int(input("Enter the num  : "))

for i in range(n):
    for j in range(i+1):
        print(" * ", end="")
    print("\n")

print("\n")
for i in range(n,0,-1):
    for j in range(i):
        print(" * ", end="")
    print("\n")


print("\n")
m=(2*n)-2
for i in range(0,n):
    for space in range(0,m):
        print(end=" ")
    m=m-1
    for j in range(0,i+1):
        print("*",end=" ")
    print("")

print("\n")
k=2*n-2
for i in range(n,-1,-1):
    for j in range(k,0,-1):
       print(end=" ")
    k=k+1
    for j in range(0,i+1):
        print("*",end=" ")
    print("")

print("\n")
k=2*n-2
for i in range(0,n):
    for j in range(0,k):
       print(end=" ")
    k=k-1
    for j in range(0,i+1):
        print("* ",end="")
    print("")
k=n-2
for i in range(n,-1,-1):
    for j in range(k,0,-1):
        print(end=" ")
    k=k+1
    for j in range(0,i+1):
        print("* ",end="")
    print("")
