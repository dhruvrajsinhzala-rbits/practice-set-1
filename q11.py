'''Given a list of numbers, create a function
to find the sum of all positive numbers.
'''
def positive_sum(l):
    p=0
    for i in l:
        if i>0:
            p+=i
    return p
l=list()
n=int(input("Enter the number of elements:- "))
for i in range(n):
    try:
        num=int(input("Enter a number:- "))
        l.append(num)
    except ValueError:
        print("Invalid input.")
print(f"Sum:- {positive_sum(l)}")