'''Implement a program that swaps the values of two variables.
'''
while True:
    try:
        x=int(input("Enter value of x:- "))
        y=int(input("Enter value of y:- "))
    except ValueError:
        print("Invalid input.")
    else:
        x=x-y
        y=x+y
        x=y-x
        print(f"Value of x:- {x}")
        print(f"Value of y:- {y}")
        break