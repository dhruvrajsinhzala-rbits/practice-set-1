'''Implement a program that checks if a given string is a palindrome
'''
def check(s):
    if s == s[::-1]:
        return True
    else:
        return False
s=input("Enter a string:- ")
if check(s):
    print(f"{s} is palindrome.")
else:
    print(f"{s} is not palindrome.")