'''Create a Python function to check if a given string is a palindrome
'''
string = input("Enter a string:- ")
if string == string[::-1]:
    print(f"{string} is palindrome.")
else:
    print(f"{string} is not palindrome.")