number = input("Enter a number and I will tell you if it is odd or even: ")

remainder = int(number) % 2

if (int(number) % 4) == 0:
    print("The number is even and divisible by 4.")
elif (int(number) % 2) == 1:
    print("The number is odd.")
else:
    print("The number is even.")
