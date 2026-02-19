'''Given a list of integers, find the sum of all positive numbers
'''
l=list()
n=int(input("Enter the number of elements:- "))
for i in range(n):
    try:
        num=int(input("Enter a number:- "))
        l.append(num)
    except ValueError:
        print("Invalid input.")
p=0
for i in l:
    if i>0:
        p+=i
print(f"The sum of all positive numbers is:- {p}")