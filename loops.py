# Question 1
for x in range(1500, 2700):
    if(x % 7 == 0) and (x % 5 == 0):
    print(x)
# Question 2
celsius = float(input("Enter the temperature in celcius:"))
    f = (celsius*1.8)+32
    print("Temperature in farenheit is:", f)
# Question 3
for i in range(1, 5):
    for j in range(1, 5):
        if j <= i:
            print("*", end="")
        else:
     print("")

     print()

 for i in range(n, 0, -1):
     for j in range(i):
     print('* ', end="")
     print('')
# Question 5
for x in range(6):
     if (x == 3 or x == 6):
         continue
     print(x, end=' ')
     print("\n")
#Question 6
    x, y = 0, 1
     while y < 50:
     print(y)
     x, y = y, x+y
#Question 10
        sum(x, y):
        sum = x + y
    if sum in range(15, 20):
        return 20
    else:
        return sum

    print(sum(10, 5))
    print(sum(9, 4))
    print(sum(12, 11))

