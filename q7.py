'''Write a program that converts a given number of days into years, weeks, and days
'''
while True:
    try:
        days = int(input("Enter days:- "))
    except ValueError:
        print("Invalid input.")
    else:
        if days <0:
            print("Invalid input.")
            continue
        else:
            year= days // 365
            days%=365
            week=days//7
            days%=7
            print(f"{year} year,{week} weeks,and {days} days.")
            break