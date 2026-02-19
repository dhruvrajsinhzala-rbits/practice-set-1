'''Create a function to reverse a given string
'''
def reverse(s):
    return s[::-1]
s=input("Enter a string:- ")
print(f"Reverse of {s} is:- {reverse(s)}")