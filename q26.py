'''Implement a program that prints the multiplication table of a given number'''
while True:
    try:
        n=int(input("Enter a number:- "))
    except ValueError:
        print("Invalid input.")
    else:
        for i in range(1,11):
            print(f"{n} x {i} = {n*i}")
        break