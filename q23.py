'''Write a Python program to check if a given number is a prime number
'''
x=int(input("Enter a number:- "))
if x < 2:
    print(f"{x} is not prime.")
else:
    for i in range(2, x):
        if x % i == 0:
            print(f"{x} is not prime.")
            break
    else:
        print(f"{x} is prime.")