'''Create a program that generates the Fibonacci sequence up to a given number of terms)
'''
n=int(input("Enter the range:- "))
a=0
b=1
for i in range(n):
    print(a, end=" ")
    a,b=b,a+b