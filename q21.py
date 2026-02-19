'''Create a program that takes a year as input and checks if it is a leap year or not
'''
while True:
    try:
        y=int(input("Enter a year:- "))
    except ValueError:
        print("Invalid input.")
    else:
        if (y%4==0 and y%100!=0) or y%400==0:
            print(f"{y} is a leap year.")
        else:
            print(f"{y} is not a leap year.")
        break