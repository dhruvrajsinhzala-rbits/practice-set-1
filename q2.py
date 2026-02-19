'''Create a program that takes a user's 
name and age as input and prints a greeting message
'''
while True:
    name = input("Please enter your name:- ")
    age = input("Please enter your age:- ")
    if not name or not age.isdigit():
        print("Invalid input. Please try again.")
    else:
        break
print(f"Hello {name}, you are {age} years old!")