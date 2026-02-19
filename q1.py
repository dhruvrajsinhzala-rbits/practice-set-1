'''Write a Python program to calculate the area 
of a rectangle given its length and width'''
while True:
    length = float(input("Enter the length of the rectangle:- "))
    width = float(input("Enter the width of the rectangle:- "))
    if length <= 0 or width <= 0:
        print("Length and width must be positive numbers. Please try again.")
    else:
        break
area = length * width
print(f"The area of the rectangle is:- {area}")