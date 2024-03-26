n = int(input("Enter the number of elements: "))
total = 0
for i in range(n):
    num = float(input("Enter number: "))
    total += num

average = total / n
print("The average is:", average)