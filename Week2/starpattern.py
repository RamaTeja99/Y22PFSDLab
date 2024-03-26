n = int(input("Enter number of astriks you need:"))
x = 1
for i in range(n):
    print("*"*x)
    x = x+1
x = n-1
for i in range(n):
     print("*"*x)
     x = x-1